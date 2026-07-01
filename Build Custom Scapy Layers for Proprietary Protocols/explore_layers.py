# File: explore_layers.py
#!/usr/bin/env python3

from scapy.all import *
from scapy.fields import *
from scapy.packet import Packet

def explore_tcp_layer():
    """
    Explore the TCP layer structure to understand Scapy's architecture.
    
    TODO: Create a TCP packet and display its structure
    TODO: Iterate through fields_desc and print field names and types
    TODO: Create a sample IP/TCP packet and show its layers
    """
    pass

def explore_field_types():
    """
    Examine different Scapy field types.
    
    TODO: Create examples of ByteField, IntField, ShortField
    TODO: Show how XIntField displays hex values
    TODO: Demonstrate StrField and StrFixedLenField
    """
    pass

if __name__ == "__main__":
    explore_tcp_layer()
    explore_field_types()
