# File: secure_comm_protocol.py
#!/usr/bin/env python3

from scapy.all import *
from scapy.fields import *
from scapy.packet import Packet
import struct

class SecureCommHeader(Packet):
    """
    Custom SecureComm Protocol Layer
    
    TODO: Define the protocol name
    TODO: Create fields_desc list with all protocol fields
    TODO: Use appropriate field types for each field
    TODO: Implement ByteEnumField for msg_type with values:
          1: "HELLO", 2: "DATA", 3: "ACK", 4: "CLOSE"
    """
    
    name = "SecureComm"
    
    fields_desc = [
        # TODO: Add XIntField for magic number (default 0x53434D4D)
        # TODO: Add ByteField for version (default 1)
        # TODO: Add ByteEnumField for msg_type
        # TODO: Add IntField for sequence
        # TODO: Add ShortField for payload_len
        # TODO: Add XShortField for checksum
    ]
    
    def post_build(self, pkt, pay):
        """
        Calculate payload length and checksum after packet construction.
        
        TODO: Update payload_len if it's 0 and payload exists
        TODO: Calculate checksum as sum of all bytes & 0xFFFF
        TODO: Return modified packet + payload
        """
        # TODO: Implement post-build logic
        return pkt + pay

# TODO: Bind the layer to UDP port 9999
# bind_layers(UDP, SecureCommHeader, dport=9999)

def test_protocol():
    """
    Test the SecureComm protocol implementation.
    
    TODO: Create HELLO packet with msg_type=1
    TODO: Create DATA packet with msg_type=2
    TODO: Display both packets using show()
    TODO: Send packets to localhost:9999
    """
    pass

if __name__ == "__main__":
    test_protocol()
