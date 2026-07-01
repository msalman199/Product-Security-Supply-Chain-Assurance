#!/usr/bin/env python3
from scapy.all import *

def capture_tcp_only(interface, count=10):
    """
    Capture only TCP packets.
    
    Args:
        interface: Network interface name
        count: Number of packets to capture
    
    Returns:
        List of captured packets
    """
    # TODO: Define packet handler for TCP packets
    # TODO: Use sniff() with filter="tcp"
    # TODO: Return captured packets
    pass

def capture_http_traffic(interface, count=10):
    """
    Capture HTTP traffic on port 80.
    
    Args:
        interface: Network interface name
        count: Number of packets to capture
    
    Returns:
        List of captured packets
    """
    # TODO: Define handler to check for port 80
    # TODO: Extract HTTP payload if present (Raw layer)
    # TODO: Use sniff() with filter="tcp port 80"
    pass

def capture_dns_queries(interface, count=10):
    """
    Capture DNS queries and responses.
    
    Args:
        interface: Network interface name
        count: Number of packets to capture
    
    Returns:
        List of captured packets
    """
    # TODO: Define handler for DNS packets
    # TODO: Check for DNS layer in packet
    # TODO: Extract query name (qd.qname) or answer (an.rdata)
    # TODO: Use sniff() with filter="udp port 53"
    pass

def main():
    interface = "eth0"
    
    # TODO: Capture TCP packets
    # TODO: Capture HTTP traffic
    # TODO: Capture DNS queries
    # TODO: Save each capture to separate PCAP files
    
    print("Filtered capture complete")

if __name__ == "__main__":
    main()
