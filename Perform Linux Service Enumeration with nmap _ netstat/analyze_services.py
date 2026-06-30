#!/usr/bin/env python3

import json
import glob

def analyze_common_services():
    """Analyze and categorize discovered services"""
    
    common_services = {
        22: "SSH",
        23: "Telnet", 
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        993: "IMAPS",
        995: "POP3S",
        3306: "MySQL",
        5432: "PostgreSQL",
        6379: "Redis",
        27017: "MongoDB"
    }
    
    # Find JSON report files
    json_files = glob.glob("*/enumeration_report_*.json")
    
    for json_file in json_files:
        print(f"Analyzing: {json_file}")
        
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        print("Identified Services:")
        print("-" * 20)
        
        for port_info in data.get('open_ports', []):
            port = int(port_info['port'])
            service_name = common_services.get(port, "Unknown")
            
            print(f"Port {port}: {service_name} ({port_info['service']})")
            
            # Security recommendations
            if port == 23:
                print("  WARNING: Telnet is insecure, consider using SSH")
            elif port == 21:
                print("  WARNING: FTP may be insecure, consider SFTP")
            elif port == 80:
                print("  INFO: HTTP detected, ensure HTTPS is also available")
        
        print()

if __name__ == "__main__":
    analyze_common_services()
