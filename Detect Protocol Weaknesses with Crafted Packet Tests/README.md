<div align="center">

# 🎯 Detect Protocol Weaknesses with Crafted Packet Tests

### Systematic Protocol Vulnerability Testing & Automated Scanning 

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scapy](https://img.shields.io/badge/Scapy-Packet_Crafting-1E88E5?style=for-the-badge)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04_LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![tcpdump](https://img.shields.io/badge/tcpdump-Traffic_Capture-14354C?style=for-the-badge)
![Fuzzing](https://img.shields.io/badge/Fuzzing-Vulnerability_Discovery-8B0000?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Protocol_Security_Testing-CC0000?style=for-the-badge)

</div>

---

> ⚠️ **AUTHORIZED USE ONLY**
> This lab is intended strictly for **educational purposes** within the Al Nafi training environment, using a locally hosted, intentionally vulnerable test server. Only test protocols and systems you own or have explicit written authorization to assess. Unauthorized testing is illegal and unethical.

---

## 📑 Table of Contents

- [🧰 Technology Stack](#-technology-stack)
- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment](#️-lab-environment)
- [📁 Directory Structure](#-directory-structure)
- [🔄 Testing Workflow](#-testing-workflow)
- [🖧 Task 1: Set Up Test Environment and Create Target Protocol](#-task-1-set-up-test-environment-and-create-target-protocol)
- [🔨 Task 2: Craft Packets to Test Protocol Weaknesses](#-task-2-craft-packets-to-test-protocol-weaknesses)
- [🤖 Task 3: Automate Protocol Security Testing](#-task-3-automate-protocol-security-testing)
- [🛡️ Vulnerability & MITRE ATT&CK Reference](#️-vulnerability--mitre-attck-reference)
- [🧯 Troubleshooting](#-troubleshooting)
- [✅ Expected Outcomes](#-expected-outcomes)
- [📌 Key Takeaways](#-key-takeaways)
- [🚀 Next Steps](#-next-steps)

---

## 🧰 Technology Stack

| Technology | Purpose | Badge |
|---|---|---|
| **Python 3.10+** | Core language for the vulnerable server, crafters, and scanners | ![Python](https://img.shields.io/badge/Python-Automation-3776AB?style=flat-square&logo=python&logoColor=white) |
| **Scapy** | Packet crafting and protocol traffic analysis | ![Scapy](https://img.shields.io/badge/Scapy-Packet_Crafting-1E88E5?style=flat-square) |
| **colorama** | Colored terminal output for test result readability | ![colorama](https://img.shields.io/badge/colorama-CLI_Formatting-000000?style=flat-square) |
| **tabulate** | Formatted vulnerability report tables | ![tabulate](https://img.shields.io/badge/tabulate-Report_Tables-4B8BBE?style=flat-square) |
| **tcpdump / netcat** | Manual traffic verification and connectivity testing | ![Networking](https://img.shields.io/badge/Networking-Traffic_Tools-14354C?style=flat-square) |
| **Ubuntu 22.04 LTS** | Target operating system and cloud lab base image | ![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04_LTS-E95420?style=flat-square&logo=ubuntu&logoColor=white) |

---

## 🎯 Objectives

| # | Objective |
|---|---|
| 1 | Craft custom network packets using Scapy to test protocol implementations |
| 2 | Identify common protocol vulnerabilities through systematic testing |
| 3 | Automate protocol security testing with Python scripts |
| 4 | Analyze protocol responses to detect security weaknesses |
| 5 | Document and report discovered vulnerabilities |

---

## 📋 Prerequisites

| # | Requirement |
|---|---|
| 1 | Basic understanding of TCP/IP networking and the OSI model |
| 2 | Familiarity with Python programming (functions, loops, error handling) |
| 3 | Basic Linux command line skills |
| 4 | Understanding of network packet structure |

---

## 🖥️ Lab Environment

> 💡 Al Nafi provides pre-configured Linux cloud machines. Click **Start Lab** to access your environment with:

| Component | Details |
|---|---|
| OS | Ubuntu 22.04 LTS |
| Runtime | Python 3.10+ |
| Library | Scapy library pre-installed |
| Tooling | Network utilities (`tcpdump`, `netcat`) |

---

## 📁 Directory Structure

```
protocol-weakness-lab/
├── protocol_server.py           # Intentionally vulnerable protocol server
├── packet_crafter.py            # Manual packet crafting + vulnerability tests
├── automated_scanner.py         # Automated test suite runner
├── test_config.json             # Test scope & payload configuration
├── traffic_analyzer.py          # Scapy-based capture & pattern analysis
└── reports/
    └── vulnerability_report.json
```

---

## 🔄 Testing Workflow

```
        ┌────────────────────────┐
        │   protocol_server.py     │
        │  (0xDEAD / 0xBEEF proto) │
        └────────────┬─────────────┘
                     │  listens on :8888
        ┌────────────┴─────────────┐
        ▼                           ▼
┌───────────────────┐     ┌───────────────────┐
│  packet_crafter.py  │     │ traffic_analyzer.py │
│ (manual crafted     │     │ (Scapy sniff on lo)  │
│  test cases)         │     └──────────┬────────┘
└──────────┬──────────┘                │
           │                            │
           ▼                            ▼
┌────────────────────────────────────────────┐
│            automated_scanner.py               │
│  (test_config.json → full test suite runner)  │
└────────────────────┬─────────────────────────┘
                     ▼
        ┌────────────────────────┐
        │  vulnerability_report.json │
        │  (severity-ranked findings) │
        └────────────────────────┘
```

---

## 🖧 Task 1: Set Up Test Environment and Create Target Protocol

### ✅ Step 1: Verify Environment Setup

Check that required tools are installed:

```bash
# Verify Python and Scapy
python3 --version
python3 -c "from scapy.all import *; print('Scapy ready')"

# Install additional dependencies if needed
pip3 install colorama tabulate
```

### 🐛 Step 2: Create a Vulnerable Protocol Server

Create `protocol_server.py` — a simple server with intentional vulnerabilities for testing:

```python
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
```

**💡 Implementation Hints:**
- Use `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` for TCP
- Valid magic number is `0xDEAD`, response magic is `0xBEEF`
- Command `999` should leak sensitive information (intentional vulnerability)
- Test buffer overflow when length field exceeds `1000`

### ▶️ Step 3: Start the Test Server

Run your server in a separate terminal:

```bash
python3 protocol_server.py
```

⚠️ **Note:** Keep this running throughout the lab.

---

## 🔨 Task 2: Craft Packets to Test Protocol Weaknesses

### 🛠️ Step 1: Create Basic Packet Crafter

Create `packet_crafter.py`:

```python
#!/usr/bin/env python3
from scapy.all import *
import struct
import socket
from colorama import Fore, Style, init

init()

class ProtocolTester:
    """Test suite for proprietary protocol vulnerability assessment."""

    def __init__(self, target_ip='127.0.0.1', target_port=8888):
        self.target_ip = target_ip
        self.target_port = target_port
        self.results = []

    def craft_packet(self, magic=0xDEAD, version=1, command=1, payload=b"test"):
        """
        Craft a protocol packet with specified parameters.

        Args:
            magic: Protocol magic number (2 bytes)
            version: Protocol version (2 bytes)
            command: Command code (2 bytes)
            payload: Payload data (bytes)

        Returns:
            Complete packet as bytes

        TODO: Pack header using struct.pack('!HHHH', ...)
        TODO: Calculate payload length
        TODO: Concatenate header + payload
        TODO: Return complete packet
        """
        pass

    def send_packet(self, packet):
        """
        Send packet via TCP and receive response.

        TODO: Create TCP socket
        TODO: Connect to target
        TODO: Send packet
        TODO: Receive response (up to 4096 bytes)
        TODO: Close socket
        TODO: Return response
        """
        pass

    def test_valid_commands(self):
        """
        Test standard protocol commands.

        TODO: Test command 1 (echo) with payload "Hello"
        TODO: Test command 2 (status) with empty payload
        TODO: Test command 3 (invalid) to see error handling
        TODO: Print results for each test
        """
        pass

    def test_invalid_magic(self):
        """
        Test protocol behavior with invalid magic numbers.

        TODO: Test with magic numbers: 0x0000, 0xFFFF, 0x1234
        TODO: Check if server validates magic number
        TODO: Document responses
        """
        pass

if __name__ == "__main__":
    # TODO: Create tester instance
    # TODO: Run test_valid_commands()
    # TODO: Run test_invalid_magic()
    pass
```

### ▶️ Step 2: Test Basic Protocol Functionality

Run your packet crafter:

```bash
python3 packet_crafter.py
```

**🎯 Expected observations:**
- Valid commands should return proper responses
- Invalid magic numbers should be rejected
- Response format should match protocol specification

### 🕵️ Step 3: Implement Vulnerability Tests

Add vulnerability detection methods to your `ProtocolTester` class:

```python
def test_authentication_bypass(self):
    """
    Scan for hidden administrative commands.

    TODO: Loop through command numbers 990-1000
    TODO: Send packets with each command number
    TODO: Check responses for keywords: "ADMIN", "password", "root"
    TODO: Flag any commands that leak sensitive information
    """
    pass

def test_buffer_overflow(self):
    """
    Test for buffer overflow vulnerabilities.

    TODO: Create packet with length field = 2000
    TODO: Create packet with actual payload of 100 bytes
    TODO: Send mismatched length/payload packet
    TODO: Check if server crashes or returns error
    """
    pass

def test_command_injection(self):
    """
    Test for command injection vulnerabilities.

    TODO: Create payloads with shell metacharacters:
          - "; ls -la"
          - "| whoami"
          - "&& cat /etc/passwd"
    TODO: Send each payload in command 1 (echo)
    TODO: Check if responses contain command output
    """
    pass
```

---

## 🤖 Task 3: Automate Protocol Security Testing

### ⚙️ Step 1: Create Automated Testing Framework

Create `automated_scanner.py`:

```python
#!/usr/bin/env python3
import struct
import socket
import time
import json
from datetime import datetime
from tabulate import tabulate

class AutomatedProtocolScanner:
    """
    Comprehensive automated protocol vulnerability scanner.
    """

    def __init__(self, target_ip='127.0.0.1', target_port=8888):
        self.target_ip = target_ip
        self.target_port = target_port
        self.vulnerabilities = []
        self.test_results = []

    def load_test_config(self, config_file='test_config.json'):
        """
        Load test configuration from JSON file.

        TODO: Read JSON configuration file
        TODO: Parse test parameters
        TODO: Return configuration dictionary
        """
        pass

    def run_test_suite(self, test_config):
        """
        Execute complete test suite based on configuration.

        TODO: Iterate through enabled tests in config
        TODO: Execute each test method
        TODO: Collect results
        TODO: Generate summary report
        """
        pass

    def fuzz_protocol(self, iterations=100):
        """
        Perform protocol fuzzing with random inputs.

        TODO: Generate random magic numbers
        TODO: Generate random command numbers
        TODO: Generate random payload sizes
        TODO: Send fuzzed packets and monitor responses
        TODO: Detect crashes or unexpected behavior
        """
        pass

    def generate_report(self):
        """
        Generate comprehensive vulnerability report.

        TODO: Summarize all vulnerabilities found
        TODO: Categorize by severity (Critical/High/Medium/Low)
        TODO: Include test statistics
        TODO: Format as table using tabulate
        TODO: Save to JSON file
        """
        pass

if __name__ == "__main__":
    # TODO: Create scanner instance
    # TODO: Load configuration
    # TODO: Run test suite
    # TODO: Generate report
    pass
```

### 📝 Step 2: Create Test Configuration File

Create `test_config.json`:

```json
{
  "tests": {
    "basic_functionality": true,
    "authentication_bypass": true,
    "buffer_overflow": true,
    "command_injection": true,
    "protocol_fuzzing": true
  },
  "payloads": {
    "command_injection": [
      "; ls -la",
      "| whoami",
      "&& cat /etc/passwd"
    ],
    "buffer_sizes": [100, 1000, 5000, 10000],
    "command_range": [1, 1000]
  },
  "timeouts": {
    "default": 5,
    "fuzzing": 2
  }
}
```

### 📡 Step 3: Implement Traffic Analysis

Create `traffic_analyzer.py`:

```python
#!/usr/bin/env python3
from scapy.all import *
import struct

class ProtocolTrafficAnalyzer:
    """
    Capture and analyze protocol traffic using Scapy.
    """

    def __init__(self, interface='lo', target_port=8888):
        self.interface = interface
        self.target_port = target_port
        self.packets = []

    def packet_callback(self, packet):
        """
        Process each captured packet.

        TODO: Check if packet has TCP layer
        TODO: Filter for target port
        TODO: Extract payload if present
        TODO: Parse protocol header
        TODO: Store packet information
        """
        pass

    def start_capture(self, duration=30):
        """
        Start packet capture for specified duration.

        TODO: Use scapy.sniff() with:
              - iface=self.interface
              - filter=f"tcp port {self.target_port}"
              - prn=self.packet_callback
              - timeout=duration
        """
        pass

    def analyze_patterns(self):
        """
        Analyze captured traffic for patterns and anomalies.

        TODO: Count command frequencies
        TODO: Identify unusual magic numbers
        TODO: Calculate payload size statistics
        TODO: Detect potential attacks in traffic
        """
        pass

if __name__ == "__main__":
    # TODO: Create analyzer
    # TODO: Start capture
    # TODO: Analyze patterns
    # TODO: Print report
    pass
```

### ▶️ Step 4: Run Complete Test Suite

Execute your automated scanner:

```bash
# Run scanner
python3 automated_scanner.py

# In another terminal, capture traffic
sudo python3 traffic_analyzer.py
```

---

## 🛡️ Vulnerability & MITRE ATT&CK Reference

| Test / Vulnerability | CWE ID | Related ATT&CK Technique | Tactic |
|---|---|---|---|
| Hidden Administrative Command (Credential Leak) | CWE-912 / CWE-200 | [T1552 – Unsecured Credentials](https://attack.mitre.org/techniques/T1552/) | Credential Access |
| Buffer Overflow (length/payload mismatch) | CWE-120 | [T1203 – Exploitation for Client Execution](https://attack.mitre.org/techniques/T1203/) | Execution |
| Command Injection Payload Testing | CWE-78 | [T1059 – Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/) | Execution |
| Missing Input Validation (magic number) | CWE-20 | [T1190 – Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) | Initial Access |
| Protocol Fuzzing Campaign | — | [T1595.002 – Active Scanning: Vulnerability Scanning](https://attack.mitre.org/techniques/T1595/002/) | Reconnaissance |

---

## 🧯 Troubleshooting

<details>
<summary>🔴 "Permission Denied" When Running Scapy</summary>

- Run with `sudo` or add user to appropriate group
- Alternative: Use `conf.L3socket=L3RawSocket` for non-root operation

</details>

<details>
<summary>🟠 Server Not Responding to Packets</summary>

- Check server is running: `netstat -tlnp | grep 8888`
- Verify firewall rules: `sudo iptables -L`
- Test connectivity: `nc -zv 127.0.0.1 8888`

</details>

<details>
<summary>🟡 Packets Not Captured by Traffic Analyzer</summary>

- Use correct interface: `ip link show` to list interfaces
- Check capture filter syntax
- Run with `sudo` for packet capture permissions

</details>

<details>
<summary>🟢 Struct Unpacking Errors</summary>

- Verify packet length before unpacking: `if len(data) >= 8:`
- Use correct format string: `!HHHH` for network byte order
- Handle exceptions with try/except blocks

</details>

---

## ✅ Expected Outcomes

| Deliverable | Description |
|---|---|
| 🛡️ Vulnerabilities Identified | Hidden admin command (999) leaking credentials, buffer overflow when length > 1000, lack of magic number validation |
| 🛠️ Testing Tools Created | Basic packet crafter, automated vulnerability scanner, traffic analysis tool |
| 📄 Reports Generated | Discovered vulnerabilities with severity ratings, test execution statistics, traffic pattern analysis |
| 🧠 Techniques Learned | Protocol reverse engineering, systematic vulnerability assessment, automated security testing |

---

## 📌 Key Takeaways

| Principle | Description |
|---|---|
| Dual-Side Validation | Always validate input on both client and server sides |
| Hidden Functionality Risk | Hidden functionality (like command 999) creates security risks |
| Automation Speed | Automated testing reveals vulnerabilities faster than manual testing |
| Defense in Depth | Protocol security requires defense in depth |

---

## 🚀 Next Steps

- Apply these techniques to real-world protocol testing
- Expand test coverage with additional vulnerability checks
- Integrate with CI/CD pipelines for continuous security testing
- Study secure protocol design principles to prevent vulnerabilities

> ⚠️ **Remember:** Only test protocols you have permission to assess. Unauthorized testing is illegal and unethical.

---

<div align="center">

**Built with ❤️ for the next generation of cybersecurity professionals.**

</div>
