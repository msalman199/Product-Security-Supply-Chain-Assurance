#!/usr/bin/env python3
from scapy.all import *
import time

class PacketCapture:
    def __init__(self, interface="eth0"):
        self.interface = interface
        self.captured_packets = []
    
    def packet_handler(self, packet):
        """
        Process each captured packet.
        
        Args:
            packet: Captured packet object
        """
        # TODO: Extract timestamp
        # TODO: Check if packet has IP layer
        # TODO: Extract source and destination IPs
        # TODO: Determine protocol (TCP/UDP/ICMP)
        # TODO: Print packet information
        # TODO: Store packet in self.captured_packets
        pass
    
    def start_capture(self, count=20, timeout=30):
        """
        Start capturing packets.
        
        Args:
            count: Number of packets to capture
            timeout: Maximum capture time in seconds
        """
        print(f"Starting capture on {self.interface}")
        
        # TODO: Use sniff() with iface, prn, count, timeout parameters
        # TODO: Handle KeyboardInterrupt for early stop
        # TODO: Print capture statistics
        pass
    
    def analyze_packets(self):
        """
        Analyze captured packets and generate statistics.
        """
        # TODO: Count packets by protocol (TCP/UDP/ICMP)
        # TODO: Identify top source IPs
        # TODO: Identify top destination ports
        # TODO: Print analysis results
        pass
    
    def save_capture(self, filename="captured.pcap"):
        """
        Save captured packets to file.
        
        Args:
            filename: Output PCAP filename
        """
        # TODO: Use wrpcap() to save packets
        pass

def main():
    # TODO: Get available interfaces using get_if_list()
    # TODO: Create PacketCapture instance
    # TODO: Start capture
    # TODO: Analyze captured packets
    # TODO: Save to file
    
    print("Capture complete")

if __name__ == "__main__":
    main()
