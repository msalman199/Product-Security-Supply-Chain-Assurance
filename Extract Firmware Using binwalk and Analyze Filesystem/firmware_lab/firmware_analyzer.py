#!/usr/bin/env python3
"""
Firmware Analysis Automation Script
"""

import os
import subprocess
import sys
import json
from pathlib import Path

class FirmwareAnalyzer:
    def __init__(self, firmware_path):
        self.firmware_path = Path(firmware_path)
        self.output_dir = Path(f"analysis_{self.firmware_path.stem}")
        self.results = {}
        
    def run_binwalk_analysis(self):
        """Run binwalk analysis on firmware"""
        print(f"[+] Analyzing firmware: {self.firmware_path}")
        
        try:
            # Run binwalk analysis
            result = subprocess.run(
                ['binwalk', str(self.firmware_path)],
                capture_output=True,
                text=True,
                check=True
            )
            
            self.results['binwalk_output'] = result.stdout
            print("[+] Binwalk analysis completed")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"[-] Binwalk analysis failed: {e}")
            return False
    
    def extract_firmware(self):
        """Extract firmware components"""
        print("[+] Extracting firmware components...")
        
        try:
            # Create output directory
            self.output_dir.mkdir(exist_ok=True)
            
            # Extract firmware
            result = subprocess.run(
                ['binwalk', '-e', '-C', str(self.output_dir), str(self.firmware_path)],
                capture_output=True,
                text=True,
                check=True
            )
            
            print("[+] Firmware extraction completed")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"[-] Firmware extraction failed: {e}")
            return False
    
    def analyze_extracted_files(self):
        """Analyze extracted files for security issues"""
        print("[+] Analyzing extracted files...")
        
        extracted_dir = self.output_dir / f"_{self.firmware_path.name}.extracted"
        
        if not extracted_dir.exists():
            print("[-] No extracted directory found")
            return False
        
        security_findings = {
            'config_files': [],
            'credentials': [],
            'private_keys': [],
            'executables': [],
            'web_files': []
        }
        
        # Find configuration files
        for config_file in extracted_dir.rglob("*.conf"):
            security_findings['config_files'].append(str(config_file))
        
        for config_file in extracted_dir.rglob("*.cfg"):
            security_findings['config_files'].append(str(config_file))
        
        # Search for credential files
        for passwd_file in extracted_dir.rglob("*passwd*"):
            security_findings['credentials'].append(str(passwd_file))
        
        # Find private keys
        for key_file in extracted_dir.rglob("*.key"):
            security_findings['private_keys'].append(str(key_file))
        
        for pem_file in extracted_dir.rglob("*.pem"):
            security_findings['private_keys'].append(str(pem_file))
        
        # Find executables
        for exe_file in extracted_dir.rglob("*"):
            if exe_file.is_file() and os.access(exe_file, os.X_OK):
                security_findings['executables'].append(str(exe_file))
        
        # Find web files
        for web_file in extracted_dir.rglob("*.php"):
            security_findings['web_files'].append(str(web_file))
        
        for web_file in extracted_dir.rglob("*.cgi"):
            security_findings['web_files'].append(str(web_file))
        
        self.results['security_findings'] = security_findings
        print("[+] File analysis completed")
        return True
    
    def search_hardcoded_secrets(self):
        """Search for hardcoded secrets in extracted files"""
        print("[+] Searching for hardcoded secrets...")
        
        extracted_dir = self.output_dir / f"_{self.firmware_path.name}.extracted"
        secrets_found = []
        
        if not extracted_dir.exists():
            return False
        
        # Search patterns for common secrets
        patterns = [
            'password',
            'passwd',
            'secret',
            'api_key',
            'private_key'
        ]
        
        try:
            for pattern in patterns:
                result = subprocess.run(
                    ['grep', '-r', '-i', pattern, str(extracted_dir)],
                    capture_output=True,
                    text=True
                )
                
                if result.stdout:
                    secrets_found.extend(result.stdout.split('\n')[:5])  # Limit results
            
            self.results['hardcoded_secrets'] = secrets_found
            print(f"[+] Found {len(secrets_found)} potential secrets")
            return True
            
        except Exception as e:
            print(f"[-] Secret search failed: {e}")
            return False
    
    def generate_report(self):
        """Generate analysis report"""
        report_file = self.output_dir / "analysis_report.json"
        
        try:
            with open(report_file, 'w') as f:
                json.dump(self.results, f, indent=2)
            
            print(f"[+] Report saved to: {report_file}")
            return True
            
        except Exception as e:
            print(f"[-] Report generation failed: {e}")
            return False
    
    def run_full_analysis(self):
        """Run complete firmware analysis"""
        print("=" * 50)
        print("FIRMWARE SECURITY ANALYSIS")
        print("=" * 50)
        
        steps = [
            self.run_binwalk_analysis,
            self.extract_firmware,
            self.analyze_extracted_files,
            self.search_hardcoded_secrets,
            self.generate_report
        ]
        
        for step in steps:
            if not step():
                print(f"[-] Analysis failed at step: {step.__name__}")
                return False
        
        print("\n[+] Analysis completed successfully!")
        self.print_summary()
        return True
    
    def print_summary(self):
        """Print analysis summary"""
        print("\n" + "=" * 30)
        print("ANALYSIS SUMMARY")
        print("=" * 30)
        
        if 'security_findings' in self.results:
            findings = self.results['security_findings']
            print(f"Configuration files found: {len(findings['config_files'])}")
            print(f"Credential files found: {len(findings['credentials'])}")
            print(f"Private keys found: {len(findings['private_keys'])}")
            print(f"Executable files found: {len(findings['executables'])}")
            print(f"Web files found: {len(findings['web_files'])}")
        
        if 'hardcoded_secrets' in self.results:
            print(f"Potential hardcoded secrets: {len(self.results['hardcoded_secrets'])}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 firmware_analyzer.py <firmware_file>")
        sys.exit(1)
    
    firmware_file = sys.argv[1]
    
    if not os.path.exists(firmware_file):
        print(f"Error: Firmware file '{firmware_file}' not found")
        sys.exit(1)
    
    analyzer = FirmwareAnalyzer(firmware_file)
    analyzer.run_full_analysis()

if __name__ == "__main__":
    main()
