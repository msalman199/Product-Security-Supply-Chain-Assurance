# File: protocol_server.py
#!/usr/bin/env python3

import socket
import struct
import threading

class ProtocolTestServer:
    """
    Simple UDP server to test SecureComm protocol
    
    TODO: Initialize socket on port 9999
    TODO: Implement receive loop
    TODO: Parse incoming SecureComm packets
    TODO: Send ACK responses
    """
    
    def __init__(self, port=9999):
        self.port = port
        self.running = False
    
    def start_server(self):
        """
        Start the UDP server.
        
        TODO: Create UDP socket
        TODO: Bind to localhost:port
        TODO: Receive and process packets
        TODO: Call process_packet for each received packet
        """
        pass
    
    def process_packet(self, data, addr):
        """
        Process received SecureComm packets.
        
        TODO: Extract magic number from data
        TODO: Verify magic == 0x53434D4D
        TODO: Parse msg_type and sequence
        TODO: Send ACK response
        """
        pass
    
    def create_ack(self, sequence):
        """
        Create ACK response packet.
        
        TODO: Build SecureComm header with msg_type=3
        TODO: Use received sequence number
        TODO: Return packed bytes
        """
        pass

if __name__ == "__main__":
    server = ProtocolTestServer()
    server.start_server()
