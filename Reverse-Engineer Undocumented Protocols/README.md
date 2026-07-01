<div align="center">

# 🧬 Reverse-Engineer Undocumented Protocols

### Custom Protocol Capture, Structure Analysis & Vulnerability Research 

![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scapy](https://img.shields.io/badge/Scapy-Protocol_Analysis-1E88E5?style=for-the-badge)
![tcpdump](https://img.shields.io/badge/tcpdump-Traffic_Capture-14354C?style=for-the-badge)
![Sockets](https://img.shields.io/badge/Sockets-TCP%2FIP-4B0082?style=for-the-badge)
![Fuzzing](https://img.shields.io/badge/Fuzzing-Vulnerability_Research-8B0000?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Difficulty-Advanced-red?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Protocol_Reverse_Engineering-CC0000?style=for-the-badge)

</div>

---

> ⚠️ **AUTHORIZED USE ONLY**
> This lab, including the exploit proof-of-concept and fuzzing tools, is provided strictly for **educational purposes** within the Al Nafi training environment, using a locally hosted test server. Capturing, reverse-engineering, exploiting, or fuzzing any protocol or system you do not own or have explicit written authorization to test is **illegal** in most jurisdictions. Never point these tools at third-party or production infrastructure.

---

## 📑 Table of Contents

- [🧰 Technology Stack](#-technology-stack)
- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment](#️-lab-environment)
- [📁 Directory Structure](#-directory-structure)
- [🔄 Analysis Workflow](#-analysis-workflow)
- [📡 Task 1: Capture Traffic from a Custom Protocol](#-task-1-capture-traffic-from-a-custom-protocol)
- [🧩 Task 2: Reverse-Engineer Protocol Structure](#-task-2-reverse-engineer-protocol-structure)
- [🛡️ Task 3: Identify Security Vulnerabilities](#️-task-3-identify-security-vulnerabilities)
- [🤖 Task 4: Automate Analysis with Scapy](#-task-4-automate-analysis-with-scapy)
- [🎯 Vulnerability & MITRE ATT&CK Reference](#-vulnerability--mitre-attck-reference)
- [🧯 Troubleshooting](#-troubleshooting)
- [✅ Expected Outcomes](#-expected-outcomes)
- [📌 Key Takeaways](#-key-takeaways)
- [🚀 Next Steps](#-next-steps)

---

## 🧰 Technology Stack

| Technology | Purpose | Badge |
|---|---|---|
| **Python 3** | Core language for the protocol server, client, and analysis tooling | ![Python](https://img.shields.io/badge/Python-Automation-3776AB?style=flat-square&logo=python&logoColor=white) |
| **Scapy** | PCAP parsing, payload extraction, and protocol dissection | ![Scapy](https://img.shields.io/badge/Scapy-Protocol_Dissection-1E88E5?style=flat-square) |
| **tcpdump** | Raw packet capture of custom protocol traffic on loopback | ![tcpdump](https://img.shields.io/badge/tcpdump-Capture-14354C?style=flat-square) |
| **socket / struct** | Low-level TCP server/client and binary field packing | ![Sockets](https://img.shields.io/badge/Sockets-Binary_Protocols-4B0082?style=flat-square) |
| **Custom Fuzzer** | Mutation-based testing of protocol fields for crash discovery | ![Fuzzing](https://img.shields.io/badge/Fuzzing-Crash_Discovery-8B0000?style=flat-square) |

---

## 🎯 Objectives

| # | Objective |
|---|---|
| 1 | Capture and analyze network traffic containing custom protocols |
| 2 | Apply reverse engineering techniques to identify protocol structure |
| 3 | Detect security vulnerabilities in proprietary protocols |
| 4 | Automate protocol analysis using Python and Scapy |
| 5 | Document protocol specifications based on traffic analysis |

---

## 📋 Prerequisites

| # | Requirement |
|---|---|
| 1 | Basic understanding of TCP/IP and network protocols |
| 2 | Familiarity with Python programming |
| 3 | Knowledge of packet capture concepts |
| 4 | Linux command line experience |

---

## 🖥️ Lab Environment

> 💡 Al Nafi provides Linux-based cloud machines with all necessary tools pre-installed. Simply click **Start Lab** to access your dedicated environment. No additional VM setup required.

---

## 📁 Directory Structure

```
protocol_lab/
├── custom_server.py            # Custom protocol TCP server
├── custom_client.py            # Custom protocol TCP client
├── protocol_capture.pcap        # Captured traffic (tcpdump)
├── protocol_analyzer.py         # Payload extraction & structure analysis
├── protocol_dissector.py        # Field-level message dissector
├── protocol_spec.py             # Auto-generated specification writer
├── protocol_spec.json           # Documented protocol specification
├── vulnerability_scanner.py     # Entropy, auth, integrity, overflow checks
├── exploit_poc.py               # Proof-of-concept exploit tests
├── automated_analyzer.py        # Pattern extraction & statistics engine
├── protocol_fuzzer.py           # Mutation-based protocol fuzzer
└── analysis_results.json        # Consolidated automated findings
```

---

## 🔄 Analysis Workflow

```
   ┌─────────────────┐        ┌─────────────────┐
   │  custom_server.py │◄──────►│  custom_client.py │
   └─────────┬─────────┘        └─────────────────┘
             │  traffic on :8888 (lo)
             ▼
   ┌─────────────────────┐
   │   tcpdump capture      │──► protocol_capture.pcap
   └─────────┬─────────────┘
             │
             ▼
   ┌─────────────────────┐     ┌─────────────────────┐
   │  protocol_analyzer.py │────►│ protocol_dissector.py │
   │  (extract payloads)    │     │ (parse fields)          │
   └─────────┬─────────────┘     └─────────┬─────────────┘
             │                              │
             ▼                              ▼
   ┌─────────────────────┐     ┌─────────────────────┐
   │ vulnerability_scanner │     │   protocol_spec.py    │──► protocol_spec.json
   │ (entropy, auth, CRC)  │     └─────────────────────┘
   └─────────┬─────────────┘
             │
             ▼
   ┌─────────────────────┐     ┌─────────────────────┐
   │    exploit_poc.py      │     │  protocol_fuzzer.py   │
   │  (authorized testing)  │     │  (crash discovery)     │
   └─────────────────────┘     └─────────────────────┘
             │                              │
             └──────────────┬───────────────┘
                            ▼
                 ┌─────────────────────┐
                 │ automated_analyzer.py │──► analysis_results.json
                 └─────────────────────┘
```

---

## 📡 Task 1: Capture Traffic from a Custom Protocol

### 📖 Overview

A custom TCP server implements a proprietary binary protocol. Traffic between the server and client is captured for structural analysis.

### 🖧 Step 1: Create Protocol Server

```bash
mkdir ~/protocol_lab && cd ~/protocol_lab
```

Create `custom_server.py`:

```python
#!/usr/bin/env python3
import socket
import struct
import threading

class CustomProtocolServer:
    def __init__(self, host='127.0.0.1', port=8888):
        self.host = host
        self.port = port

    def create_message(self, msg_type, data):
        """
        Create a custom protocol message.
        Protocol format: [MAGIC(4)][VERSION(1)][TYPE(1)][LENGTH(2)][DATA][CHECKSUM(1)]

        TODO: Implement message creation with proper field packing
        TODO: Calculate checksum as sum of data bytes % 256
        """
        pass

    def handle_client(self, client_socket, addr):
        """
        TODO: Send welcome message (type 1)
        TODO: Send status message (type 2)
        TODO: Send data message (type 3) with flag
        TODO: Implement proper error handling
        """
        pass

    def start(self):
        """
        TODO: Bind socket and listen for connections
        TODO: Accept clients and spawn handler threads
        """
        pass

if __name__ == "__main__":
    server = CustomProtocolServer()
    server.start()
```

### 💻 Step 2: Create Protocol Client

Create `custom_client.py`:

```python
#!/usr/bin/env python3
import socket

def connect_to_server():
    """
    TODO: Connect to server on localhost:8888
    TODO: Receive and display messages
    TODO: Handle connection errors gracefully
    """
    pass

if __name__ == "__main__":
    connect_to_server()
```

### 🎙️ Step 3: Capture Network Traffic

Start the server and capture traffic:

```bash
# Start server in background
python3 custom_server.py &
SERVER_PID=$!

# Start packet capture
sudo tcpdump -i lo -w protocol_capture.pcap port 8888 &
TCPDUMP_PID=$!

# Run client for 30 seconds
timeout 30 python3 custom_client.py

# Stop capture and server
sudo kill $TCPDUMP_PID
kill $SERVER_PID
```

### 🔎 Step 4: Initial Traffic Inspection

Examine captured packets:

```bash
# View packet summary
tcpdump -r protocol_capture.pcap -n

# View hex dump of first 5 packets
tcpdump -r protocol_capture.pcap -X -c 5
```

---

## 🧩 Task 2: Reverse-Engineer Protocol Structure

### 🔬 Step 1: Extract and Analyze Payloads

Create `protocol_analyzer.py`:

```python
#!/usr/bin/env python3
from scapy.all import *
import struct

class ProtocolAnalyzer:
    def __init__(self, pcap_file):
        self.pcap_file = pcap_file
        self.packets = []

    def load_packets(self):
        """
        TODO: Load packets from PCAP file using rdpcap()
        TODO: Filter for TCP packets with Raw payload
        """
        pass

    def extract_payloads(self):
        """
        TODO: Extract TCP payload data from packets
        TODO: Return list of payload byte strings
        """
        pass

    def analyze_structure(self, payloads):
        """
        TODO: Identify common patterns in first bytes (magic)
        TODO: Analyze payload length distribution
        TODO: Look for fixed-position fields
        TODO: Print hex and ASCII representation
        """
        pass

    def identify_fields(self, payload):
        """
        TODO: Parse potential magic bytes (first 4 bytes)
        TODO: Extract version field (byte 5)
        TODO: Extract message type (byte 6)
        TODO: Parse length field (bytes 7-8, big-endian)
        TODO: Extract data based on length field
        TODO: Identify checksum (last byte)
        """
        pass

if __name__ == "__main__":
    analyzer = ProtocolAnalyzer("protocol_capture.pcap")
    analyzer.load_packets()
    payloads = analyzer.extract_payloads()
    analyzer.analyze_structure(payloads)
```

### 🧷 Step 2: Create Protocol Dissector

Create `protocol_dissector.py`:

```python
#!/usr/bin/env python3
import struct

class ProtocolDissector:
    def __init__(self):
        self.message_types = {
            1: "WELCOME",
            2: "STATUS",
            3: "DATA"
        }

    def dissect_message(self, payload):
        """
        Dissect a protocol message into its components.

        Returns dict with fields:
        - magic: 4-byte identifier
        - version: protocol version
        - type: message type code
        - type_name: human-readable type
        - length: data length
        - data: message data
        - checksum: integrity check value
        - checksum_valid: boolean validation result

        TODO: Implement field extraction
        TODO: Validate checksum (sum of data bytes % 256)
        TODO: Handle parsing errors
        """
        pass

    def analyze_all_messages(self, payloads):
        """
        TODO: Dissect all payloads
        TODO: Count message types
        TODO: Identify patterns and anomalies
        """
        pass

if __name__ == "__main__":
    # TODO: Load payloads and analyze
    pass
```

### 📝 Step 3: Document Protocol Specification

Create `protocol_spec.py`:

```python
#!/usr/bin/env python3
import json

def generate_protocol_documentation(analysis_results):
    """
    Generate protocol specification document.

    TODO: Document field structure and sizes
    TODO: List message types and meanings
    TODO: Describe checksum algorithm
    TODO: Note protocol version information
    TODO: Save as JSON file
    """
    spec = {
        "protocol_name": "Custom Protocol",
        "version": "1.0",
        "fields": [
            # TODO: Add field specifications
        ],
        "message_types": {
            # TODO: Add message type definitions
        },
        "security_notes": [
            # TODO: Add security observations
        ]
    }

    with open("protocol_spec.json", "w") as f:
        json.dump(spec, f, indent=2)

    return spec
```

---

## 🛡️ Task 3: Identify Security Vulnerabilities

### 🕵️ Step 1: Automated Vulnerability Scanner

Create `vulnerability_scanner.py`:

```python
#!/usr/bin/env python3
from scapy.all import *
import math

class VulnerabilityScanner:
    def __init__(self, pcap_file):
        self.pcap_file = pcap_file
        self.vulnerabilities = []

    def calculate_entropy(self, data):
        """
        Calculate Shannon entropy to detect encryption.

        TODO: Count byte frequencies
        TODO: Calculate probability distribution
        TODO: Compute entropy: -sum(p * log2(p))
        TODO: Return entropy score (0-8)
        """
        pass

    def check_information_disclosure(self, payload):
        """
        TODO: Search for sensitive keywords (password, secret, key, flag)
        TODO: Check for plaintext credentials
        TODO: Identify exposed internal data
        """
        pass

    def check_weak_authentication(self, payload):
        """
        TODO: Identify predictable magic bytes
        TODO: Check for missing authentication fields
        TODO: Detect replay attack vulnerabilities
        """
        pass

    def check_integrity_protection(self, payload):
        """
        TODO: Analyze checksum strength
        TODO: Test for collision resistance
        TODO: Verify checksum validation
        """
        pass

    def check_buffer_overflow_risk(self, payload):
        """
        TODO: Identify oversized payloads
        TODO: Check length field validation
        TODO: Detect potential buffer overflows
        """
        pass

    def scan_all_vulnerabilities(self):
        """
        TODO: Load packets from PCAP
        TODO: Run all vulnerability checks
        TODO: Categorize by severity (Critical, High, Medium, Low)
        TODO: Generate vulnerability report
        """
        pass

    def generate_report(self):
        """
        TODO: Create formatted vulnerability report
        TODO: Include remediation recommendations
        TODO: Save to file
        """
        pass

if __name__ == "__main__":
    scanner = VulnerabilityScanner("protocol_capture.pcap")
    scanner.scan_all_vulnerabilities()
    scanner.generate_report()
```

### 💣 Step 2: Exploit Proof-of-Concept

Create `exploit_poc.py`:

```python
#!/usr/bin/env python3
import socket
import struct

class ProtocolExploit:
    def __init__(self, target_host='127.0.0.1', target_port=8888):
        self.target_host = target_host
        self.target_port = target_port

    def craft_malicious_packet(self):
        """
        Craft a packet to test vulnerabilities.

        TODO: Create packet with invalid checksum
        TODO: Test with oversized length field
        TODO: Try buffer overflow payload
        TODO: Test replay attack
        """
        pass

    def test_checksum_bypass(self):
        """
        TODO: Send packet with incorrect checksum
        TODO: Verify if server validates integrity
        """
        pass

    def test_buffer_overflow(self):
        """
        TODO: Send oversized payload
        TODO: Monitor server response
        """
        pass

    def run_exploit_tests(self):
        """
        TODO: Execute all exploit tests
        TODO: Document successful exploits
        TODO: Record server behavior
        """
        pass

# WARNING: Only run against authorized test systems
if __name__ == "__main__":
    print("Exploit testing - authorized systems only")
    # TODO: Implement safe testing framework
```

---

## 🤖 Task 4: Automate Analysis with Scapy

### ⚙️ Step 1: Create Automated Analysis Tool

Create `automated_analyzer.py`:

```python
#!/usr/bin/env python3
from scapy.all import *
from collections import defaultdict
import json

class AutomatedProtocolAnalyzer:
    def __init__(self, pcap_file):
        self.pcap_file = pcap_file
        self.results = {
            "patterns": {},
            "vulnerabilities": [],
            "statistics": {}
        }

    def extract_patterns(self):
        """
        TODO: Identify common byte sequences
        TODO: Find repeating patterns
        TODO: Detect protocol signatures
        TODO: Calculate pattern frequencies
        """
        pass

    def statistical_analysis(self):
        """
        TODO: Calculate payload length statistics (min, max, avg)
        TODO: Compute entropy distribution
        TODO: Analyze timing patterns
        TODO: Identify protocol behavior patterns
        """
        pass

    def generate_protocol_signature(self):
        """
        TODO: Create unique protocol fingerprint
        TODO: Hash common characteristics
        TODO: Generate detection rules
        """
        pass

    def export_results(self, output_file="analysis_results.json"):
        """
        TODO: Format analysis results
        TODO: Include all findings
        TODO: Save to JSON file
        """
        pass

    def run_full_analysis(self):
        """
        TODO: Execute all analysis functions
        TODO: Compile comprehensive report
        TODO: Generate actionable insights
        """
        pass

if __name__ == "__main__":
    analyzer = AutomatedProtocolAnalyzer("protocol_capture.pcap")
    analyzer.run_full_analysis()
    analyzer.export_results()
```

### 🧪 Step 2: Create Protocol Fuzzer

Create `protocol_fuzzer.py`:

```python
#!/usr/bin/env python3
import socket
import random
import struct

class ProtocolFuzzer:
    def __init__(self, target_host='127.0.0.1', target_port=8888):
        self.target_host = target_host
        self.target_port = target_port
        self.crash_cases = []

    def fuzz_magic_bytes(self):
        """
        TODO: Generate random magic byte variations
        TODO: Test server response to invalid magic
        """
        pass

    def fuzz_length_field(self):
        """
        TODO: Send mismatched length values
        TODO: Test with negative lengths
        TODO: Try maximum integer values
        """
        pass

    def fuzz_data_field(self):
        """
        TODO: Send random data patterns
        TODO: Test special characters
        TODO: Try format string attacks
        """
        pass

    def monitor_server_response(self, test_case):
        """
        TODO: Send fuzzed packet
        TODO: Monitor for crashes or errors
        TODO: Record anomalous behavior
        """
        pass

    def run_fuzzing_campaign(self, iterations=1000):
        """
        TODO: Execute fuzzing tests
        TODO: Track successful exploits
        TODO: Generate fuzzing report
        """
        pass

# WARNING: Only fuzz authorized test systems
if __name__ == "__main__":
    fuzzer = ProtocolFuzzer()
    # TODO: Implement safe fuzzing with proper authorization
```

---

## 🎯 Vulnerability & MITRE ATT&CK Reference

| Vulnerability / Technique | CWE ID | Related ATT&CK Technique | Tactic |
|---|---|---|---|
| Passive Protocol Traffic Capture | — | [T1040 – Network Sniffing](https://attack.mitre.org/techniques/T1040/) | Discovery / Collection |
| Information Disclosure (plaintext secrets) | CWE-319 | [T1552.001 – Unsecured Credentials: Credentials In Files](https://attack.mitre.org/techniques/T1552/001/) | Credential Access |
| Weak Integrity Protection (trivial checksum) | CWE-354 | [T1565 – Data Manipulation](https://attack.mitre.org/techniques/T1565/) | Impact |
| Missing Authentication for Critical Function | CWE-306 | [T1190 – Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) | Initial Access |
| Buffer Overflow via Oversized Length Field | CWE-120 | [T1203 – Exploitation for Client Execution](https://attack.mitre.org/techniques/T1203/) | Execution |
| Replay Attack (no nonce/session validation) | CWE-294 | [T1557 – Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557/) | Collection |

---

## 🧯 Troubleshooting

<details>
<summary>🔴 No Packets Captured in PCAP File</summary>

- Ensure server and client are running during capture
- Verify correct interface (use `lo` for localhost traffic)
- Check tcpdump has proper permissions (use `sudo`)

</details>

<details>
<summary>🟠 Scapy Import Errors</summary>

- Install Scapy with `pip3 install scapy`
- May need to install libpcap-dev: `sudo apt-get install libpcap-dev`

</details>

<details>
<summary>🟡 Cannot Parse Protocol Fields Correctly</summary>

- Verify byte order (big-endian vs little-endian)
- Check `struct` format strings match protocol specification
- Use hex dumps to manually verify field positions

</details>

<details>
<summary>🟢 Server Crashes During Fuzzing</summary>

- This may indicate a vulnerability — document the crash case
- Implement proper error handling in server code
- Use try-except blocks to catch parsing errors

</details>

---

## ✅ Expected Outcomes

| Deliverable | Description |
|---|---|
| 📡 Traffic Capture | Captured network traffic containing a custom protocol |
| 🧩 Structure Analysis | Reverse-engineered the protocol structure and field layout |
| 🛡️ Vulnerabilities Identified | Information disclosure, weak integrity, predictable IDs, missing encryption |
| 🤖 Automated Tooling | Created automated analysis tools using Python and Scapy |
| 📄 Documentation | Documented the complete protocol specification |
| 💣 Proof-of-Concept | Developed PoC exploits for identified vulnerabilities |

---

## 📌 Key Takeaways

| Principle | Description |
|---|---|
| Systematic Analysis | Protocol reverse engineering requires systematic analysis of traffic patterns |
| Peer Review Gap | Security vulnerabilities often exist in custom protocols due to lack of peer review |
| Automation Value | Automation tools significantly improve analysis efficiency |
| Documentation | Proper documentation is crucial for understanding protocol behavior |
| Authorization | Always obtain authorization before testing real-world systems |

---

## 🚀 Next Steps

- Continue practicing these techniques on CTF challenges
- Apply skills in authorized penetration testing engagements
- Develop deeper expertise in protocol analysis and security assessment

---

<div align="center">

**Built with ❤️ for the next generation of cybersecurity professionals.**

</div>
