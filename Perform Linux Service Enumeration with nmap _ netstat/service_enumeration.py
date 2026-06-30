#!/usr/bin/env python3

import nmap
import subprocess
import json
import datetime
import os
import sys

class ServiceEnumerator:
    def __init__(self, target="localhost"):
        self.target = target
        self.nm = nmap.PortScanner()
        self.results = {}
        self.output_dir = "enumeration_results"
        
        # Create output directory
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def nmap_scan(self):
        """Perform comprehensive nmap scanning"""
        print(f"Starting nmap scan of {self.target}...")
        
        try:
            # Basic TCP scan
            print("Performing TCP scan...")
            tcp_scan = self.nm.scan(self.target, '1-65535', '-sS')
            
            # Service version detection
            print("Performing service detection...")
            service_scan = self.nm.scan(self.target, arguments='-sV')
            
            # Script scanning
            print("Performing script scan...")
            script_scan = self.nm.scan(self.target, arguments='-sC')
            
            self.results['nmap'] = {
                'tcp_scan': tcp_scan,
                'service_scan': service_scan,
                'script_scan': script_scan
            }
            
            return True
            
        except Exception as e:
            print(f"Error during nmap scan: {e}")
            return False
    
    def netstat_analysis(self):
        """Perform netstat analysis"""
        print("Performing netstat analysis...")
        
        try:
            # Get listening ports
            listening_cmd = ["netstat", "-ln"]
            listening_result = subprocess.run(listening_cmd, capture_output=True, text=True)
            
            # Get active connections
            active_cmd = ["netstat", "-an"]
            active_result = subprocess.run(active_cmd, capture_output=True, text=True)
            
            # Get process information
            process_cmd = ["netstat", "-lnp"]
            process_result = subprocess.run(process_cmd, capture_output=True, text=True)
            
            self.results['netstat'] = {
                'listening_ports': listening_result.stdout,
                'active_connections': active_result.stdout,
                'process_info': process_result.stdout
            }
            
            return True
            
        except Exception as e:
            print(f"Error during netstat analysis: {e}")
            return False
    
    def parse_results(self):
        """Parse and analyze results"""
        print("Parsing results...")
        
        parsed_results = {
            'timestamp': datetime.datetime.now().isoformat(),
            'target': self.target,
            'open_ports': [],
            'services': [],
            'listening_ports': [],
            'active_connections': 0
        }
        
        # Parse nmap results
        if 'nmap' in self.results:
            for host in self.nm.all_hosts():
                for proto in self.nm[host].all_protocols():
                    ports = self.nm[host][proto].keys()
                    for port in ports:
                        state = self.nm[host][proto][port]['state']
                        if state == 'open':
                            service_info = {
                                'port': port,
                                'protocol': proto,
                                'state': state,
                                'service': self.nm[host][proto][port].get('name', 'unknown'),
                                'version': self.nm[host][proto][port].get('version', 'unknown')
                            }
                            parsed_results['open_ports'].append(service_info)
                            parsed_results['services'].append(service_info)
        
        # Parse netstat results
        if 'netstat' in self.results:
            listening_lines = self.results['netstat']['listening_ports'].split('\n')
            for line in listening_lines:
                if 'LISTEN' in line:
                    parts = line.split()
                    if len(parts) >= 4:
                        parsed_results['listening_ports'].append(parts[3])
            
            # Count active connections
            active_lines = self.results['netstat']['active_connections'].split('\n')
            active_count = sum(1 for line in active_lines if 'ESTABLISHED' in line)
            parsed_results['active_connections'] = active_count
        
        return parsed_results
    
    def generate_report(self, parsed_results):
        """Generate comprehensive report"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # JSON report
        json_file = f"{self.output_dir}/enumeration_report_{timestamp}.json"
        with open(json_file, 'w') as f:
            json.dump(parsed_results, f, indent=2)
        
        # Text report
        txt_file = f"{self.output_dir}/enumeration_report_{timestamp}.txt"
        with open(txt_file, 'w') as f:
            f.write("SERVICE ENUMERATION REPORT\n")
            f.write("=" * 50 + "\n")
            f.write(f"Target: {parsed_results['target']}\n")
            f.write(f"Timestamp: {parsed_results['timestamp']}\n\n")
            
            f.write("OPEN PORTS (nmap):\n")
            f.write("-" * 20 + "\n")
            for port_info in parsed_results['open_ports']:
                f.write(f"Port {port_info['port']}/{port_info['protocol']}: "
                       f"{port_info['service']} ({port_info['version']})\n")
            
            f.write(f"\nLISTENING PORTS (netstat): {len(parsed_results['listening_ports'])}\n")
            f.write("-" * 30 + "\n")
            for port in parsed_results['listening_ports']:
                f.write(f"{port}\n")
            
            f.write(f"\nACTIVE CONNECTIONS: {parsed_results['active_connections']}\n")
        
        print(f"Reports generated:")
        print(f"  JSON: {json_file}")
        print(f"  Text: {txt_file}")
    
    def run_enumeration(self):
        """Run complete enumeration process"""
        print("Starting automated service enumeration...")
        print("=" * 50)
        
        # Perform nmap scanning
        if not self.nmap_scan():
            print("nmap scanning failed")
            return False
        
        # Perform netstat analysis
        if not self.netstat_analysis():
            print("netstat analysis failed")
            return False
        
        # Parse results
        parsed_results = self.parse_results()
        
        # Generate reports
        self.generate_report(parsed_results)
        
        print("\nEnumeration completed successfully!")
        print(f"Found {len(parsed_results['open_ports'])} open ports")
        print(f"Found {len(parsed_results['listening_ports'])} listening ports")
        print(f"Found {parsed_results['active_connections']} active connections")
        
        return True

def main():
    # Create enumerator instance
    enumerator = ServiceEnumerator()
    
    # Run enumeration
    success = enumerator.run_enumeration()
    
    if success:
        print("\nService enumeration completed successfully!")
    else:
        print("\nService enumeration failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
