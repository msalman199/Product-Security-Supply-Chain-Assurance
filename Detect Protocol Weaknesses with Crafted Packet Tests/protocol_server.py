#!/usr/bin/env python3
import socket
import threading
import struct

class VulnerableProtocolServer:
    """
    A deliberately vulnerable protocol server for testing.
    Protocol format: [Magic:2][Version:2][Command:2][Length:2][Payload:N]
    """
    
    def __init__(self, host='127.0.0.1', port=8888):
        self.host = host
        self.port = port
        
    def handle_client(self, client_socket, address):
        """
        Handle incoming client connections.
        
        TODO: Implement packet reception (1024 bytes)
        TODO: Parse header using struct.unpack('!HHHH', data[:8])
        TODO: Implement command handlers:
              - Command 1: Echo payload back
              - Command 2: Return "STATUS_OK"
              - Command 999: Return admin credentials (vulnerability)
        TODO: Handle invalid magic numbers (should be 0xDEAD)
        TODO: Check for buffer overflow when length > 1000
        """
        pass
        
    def start(self):
        """
        Start the server and listen for connections.
        
        TODO: Create TCP socket
        TODO: Bind to host:port
        TODO: Listen for connections
        TODO: Accept clients in loop and spawn threads
        """
        pass

if __name__ == "__main__":
    # TODO: Create server instance and start
    pass
