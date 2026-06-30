#!/usr/bin/env python3

import nmap
import json
import datetime

class AdvancedNmapScanner:
    def __init__(self, target="localhost"):
        self.target = target
        self.nm = nmap.PortScanner()
    
    def vulnerability_scan(self):
        """Perform vulnerability scanning"""
        print("Performing vulnerability scan...")
        try:
            result = self.nm.scan(self.target, arguments='--script vuln')
            return result
        except Exception as e:
            print(f"Vulnerability scan error: {e}")
            return None
    
    def service_enumeration_scan(self):
        """Detailed service enumeration"""
        print("Performing detailed service enumeration...")
        try:
            result = self.nm.scan(self.target, arguments='-sV --script=banner,http-title,ssh-hostkey')
            return result
        except Exception as e:
            print(f"Service enumeration error: {e}")
            return None
    
    def stealth_scan(self):
        """Perform stealth scanning"""
        print("Performing stealth scan...")
        try:
            result = self.nm.scan(self.target, arguments='-sS -T2')
            return result
        except Exception as e:
            print(f"Stealth scan error: {e}")
            return None
    
    def comprehensive_scan(self):
        """Run all scanning methods"""
        results = {}
        
        # Basic scan
        print("Running basic scan...")
        results['basic'] = self.nm.scan(self.target, '1-1000')
        
        # Service scan
        results['service'] = self.service_enumeration_scan()
        
        # Vulnerability scan
        results['vulnerability'] = self.vulnerability_scan()
        
        # Stealth scan
        results['stealth'] = self.stealth_scan()
        
        return results

# Example usage
if __name__ == "__main__":
    scanner = AdvancedNmapScanner()
    results = scanner.comprehensive_scan()
    
    # Save results
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"advanced_scan_{timestamp}.json", 'w') as f:
        json.dump(results, f, indent=2)
    
    print("Advanced scanning completed!")
