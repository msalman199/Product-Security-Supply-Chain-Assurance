<div align="center">

# 📦 Craft and Capture Packets Using Scapy

### Network Packet Manipulation, Capture & Automation 

![Scapy](https://img.shields.io/badge/Scapy-Packet_Crafting-1E88E5?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![libpcap](https://img.shields.io/badge/libpcap-Packet_Capture-14354C?style=for-the-badge)
![tcpdump](https://img.shields.io/badge/tcpdump-Traffic_Inspection-14354C?style=for-the-badge)
![Ubuntu](https://img.shields.io/badge/Ubuntu-Linux-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Root Access](https://img.shields.io/badge/Privileges-Root%2FSudo-critical?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Network_Security-CC0000?style=for-the-badge)

</div>

---

> ⚠️ **AUTHORIZED USE ONLY**
> This lab is intended strictly for **educational purposes** within the Al Nafi training environment. Crafting, sending, or capturing packets against networks or hosts you do not own or have explicit written authorization to test is **illegal** in most jurisdictions. Confine all packet operations to the lab environment (localhost/lab network) unless authorized otherwise.

---

## 📑 Table of Contents

- [🧰 Technology Stack](#-technology-stack)
- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment](#️-lab-environment)
- [📁 Directory Structure](#-directory-structure)
- [🔄 Packet Workflow](#-packet-workflow)
- [🧪 Task 1: Install and Verify Scapy](#-task-1-install-and-verify-scapy)
- [🛠️ Task 2: Craft Custom Network Packets](#️-task-2-craft-custom-network-packets)
- [📡 Task 3: Capture and Analyze Network Traffic](#-task-3-capture-and-analyze-network-traffic)
- [🤖 Task 4: Automate Packet Operations](#-task-4-automate-packet-operations)
- [🛡️ Techniques & MITRE ATT&CK Reference](#️-techniques--mitre-attck-reference)
- [🧯 Troubleshooting](#-troubleshooting)
- [✅ Expected Outcomes](#-expected-outcomes)
- [📌 Key Takeaways](#-key-takeaways)
- [🚀 Next Steps](#-next-steps)

---

## 🧰 Technology Stack

| Technology | Purpose | Badge |
|---|---|---|
| **Scapy** | Python library for crafting, sending, sniffing, and dissecting packets | ![Scapy](https://img.shields.io/badge/Scapy-Packet_Manipulation-1E88E5?style=flat-square) |
| **Python 3** | Core scripting language for all packet operations | ![Python](https://img.shields.io/badge/Python-Automation-3776AB?style=flat-square&logo=python&logoColor=white) |
| **libpcap** | Underlying packet capture library used by Scapy/tcpdump | ![libpcap](https://img.shields.io/badge/libpcap-Capture_Engine-14354C?style=flat-square) |
| **tcpdump** | CLI tool for verifying and inspecting generated PCAP files | ![tcpdump](https://img.shields.io/badge/tcpdump-PCAP_Inspection-14354C?style=flat-square) |
| **Root/Sudo Privileges** | Required for raw socket access during crafting and sniffing | ![Root](https://img.shields.io/badge/Access-Root%2FSudo-critical?style=flat-square) |

---

## 🎯 Objectives

| # | Objective |
|---|---|
| 1 | Install and configure Scapy for packet manipulation |
| 2 | Craft custom network packets with various protocols |
| 3 | Capture and filter network traffic in real-time |
| 4 | Analyze packet structures and protocol behaviors |
| 5 | Automate packet operations using Python scripts |

---

## 📋 Prerequisites

| # | Requirement |
|---|---|
| 1 | Basic Python programming knowledge |
| 2 | Understanding of TCP/IP networking concepts |
| 3 | Familiarity with Linux command line |
| 4 | Knowledge of common network protocols (TCP, UDP, ICMP) |

---

## 🖥️ Lab Environment

> 💡 Al Nafi provides pre-configured Linux cloud machines. Click **Start Lab** to access your environment with:

| Component | Details |
|---|---|
| OS | Ubuntu Linux with Python 3 |
| Library | Scapy and dependencies pre-installed |
| Tooling | Network tools and utilities |
| Access | Root/sudo access for packet operations |

---

## 📁 Directory Structure

```
scapy-lab/
├── packet_crafter.py            # ICMP / TCP SYN / UDP packet crafting
├── advanced_crafter.py          # Port scan, fragmentation, custom fields
├── packet_capture.py            # Live capture with protocol analysis
├── filtered_capture.py          # TCP / HTTP / DNS filtered captures
├── packet_automation.py         # Background capture + automated testing
├── send_receive.py              # sr1() / sr() request-response testing
└── captures/
    ├── crafted_packets.pcap
    ├── captured.pcap
    ├── tcp_only.pcap
    ├── http_traffic.pcap
    ├── dns_queries.pcap
    └── automation_report_*.json
```

---

## 🔄 Packet Workflow

```
   ┌────────────────┐     ┌────────────────┐     ┌────────────────┐
   │  Craft Packet    │     │  Send / Sniff    │     │  Capture PCAP    │
   │ (IP/TCP/UDP/ICMP)│────►│ (send/sr1/sniff) │────►│ (wrpcap output)  │
   └────────────────┘     └────────────────┘     └────────┬───────┘
                                                            │
                                                            ▼
   ┌────────────────┐     ┌────────────────┐     ┌────────────────┐
   │  JSON Report     │◄────│  Analyze Traffic │◄────│  Filter/Parse    │
   │ (protocols, IPs)  │     │ (protocols, IPs)  │     │ (tcp/http/dns)    │
   └────────────────┘     └────────────────┘     └────────────────┘
```

---

## 🧪 Task 1: Install and Verify Scapy

### 📥 Step 1.1: Update System and Install Scapy

```bash
sudo apt update
sudo apt install python3-pip python3-dev libpcap-dev -y
sudo pip3 install scapy
```

### ✅ Step 1.2: Verify Installation

```bash
sudo python3 -c "from scapy.all import *; print('Scapy version:', scapy.__version__)"
```

### 🌐 Step 1.3: Identify Network Interface

```bash
ip addr show
```

💡 **Note:** Note your primary interface name (typically `eth0` or `ens3`).

---

## 🛠️ Task 2: Craft Custom Network Packets

### 🔨 Step 2.1: Create Basic Packet Crafter

Create `packet_crafter.py`:

```python
#!/usr/bin/env python3
from scapy.all import *

def craft_icmp_packet(target_ip):
    """
    Craft an ICMP echo request packet.

    Args:
        target_ip: Destination IP address

    Returns:
        Scapy packet object
    """
    # TODO: Create IP layer with destination
    # TODO: Create ICMP layer
    # TODO: Combine layers and return packet
    pass

def craft_tcp_syn_packet(target_ip, target_port):
    """
    Craft a TCP SYN packet for connection initiation.

    Args:
        target_ip: Destination IP address
        target_port: Destination port number

    Returns:
        Scapy packet object
    """
    # TODO: Create IP layer
    # TODO: Create TCP layer with SYN flag
    # TODO: Combine and return packet
    pass

def craft_udp_packet(target_ip, target_port, payload):
    """
    Craft a UDP packet with custom payload.

    Args:
        target_ip: Destination IP address
        target_port: Destination port
        payload: Data to send

    Returns:
        Scapy packet object
    """
    # TODO: Create IP layer
    # TODO: Create UDP layer
    # TODO: Add payload and return packet
    pass

def display_packet_details(packet):
    """
    Display detailed information about a packet.

    Args:
        packet: Scapy packet object
    """
    # TODO: Print packet summary
    # TODO: Use packet.show() for detailed view
    pass

def main():
    target = "127.0.0.1"

    # TODO: Craft ICMP packet and display
    # TODO: Craft TCP SYN packet and display
    # TODO: Craft UDP packet and display
    # TODO: Save packets to PCAP file using wrpcap()

    print("Packet crafting complete")

if __name__ == "__main__":
    main()
```

### 🧬 Step 2.2: Create Advanced Packet Manipulator

Create `advanced_crafter.py`:

```python
#!/usr/bin/env python3
from scapy.all import *

def create_port_scan_packets(target_ip, port_list):
    """
    Create TCP SYN packets for multiple ports.

    Args:
        target_ip: Target IP address
        port_list: List of ports to scan

    Returns:
        List of packet objects
    """
    # TODO: Loop through ports
    # TODO: Create SYN packet for each port
    # TODO: Return list of packets
    pass

def create_fragmented_packet(target_ip, payload_size):
    """
    Create and fragment a large packet.

    Args:
        target_ip: Destination IP
        payload_size: Size of payload in bytes

    Returns:
        List of fragmented packets
    """
    # TODO: Create large payload
    # TODO: Create packet with payload
    # TODO: Use fragment() function to split packet
    # TODO: Return fragments
    pass

def create_custom_fields_packet(src_ip, dst_ip, ttl_value):
    """
    Create packet with custom IP header fields.

    Args:
        src_ip: Source IP address
        dst_ip: Destination IP address
        ttl_value: Time-to-live value

    Returns:
        Packet with custom fields
    """
    # TODO: Create IP layer with custom src, dst, ttl
    # TODO: Add ICMP or TCP layer
    # TODO: Return packet
    pass

def main():
    # TODO: Create port scan packets for ports [22, 80, 443]
    # TODO: Create fragmented packet with 2000 byte payload
    # TODO: Create packet with custom TTL value
    # TODO: Save all packets to PCAP file

    print("Advanced packet crafting complete")

if __name__ == "__main__":
    main()
```

### ▶️ Step 2.3: Execute and Examine

```bash
chmod +x packet_crafter.py advanced_crafter.py
sudo python3 packet_crafter.py
sudo python3 advanced_crafter.py
```

Examine the created PCAP files using:

```bash
tcpdump -r crafted_packets.pcap -n
```

---

## 📡 Task 3: Capture and Analyze Network Traffic

### 🎙️ Step 3.1: Create Packet Capture Script

Create `packet_capture.py`:

```python
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
```

### 🎯 Step 3.2: Create Filtered Capture Script

Create `filtered_capture.py`:

```python
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
```

### 🚦 Step 3.3: Generate Test Traffic

Before capturing, generate some traffic:

```bash
# Terminal 1: Generate traffic
ping -c 10 127.0.0.1 &
curl -s http://example.com > /dev/null &
nslookup google.com &
```

```bash
# Terminal 2: Run capture
sudo python3 packet_capture.py
```

### ▶️ Step 3.4: Execute Filtered Captures

```bash
sudo python3 filtered_capture.py
```

---

## 🤖 Task 4: Automate Packet Operations

### ⚙️ Step 4.1: Create Automation Framework

Create `packet_automation.py`:

```python
#!/usr/bin/env python3
from scapy.all import *
import threading
import time
import json

class PacketAutomation:
    def __init__(self, interface="eth0"):
        self.interface = interface
        self.captured_packets = []
        self.sent_packets = []
        self.capturing = False

    def start_background_capture(self):
        """
        Start packet capture in background thread.
        """
        def capture_worker():
            # TODO: Set self.capturing to True
            # TODO: Define packet handler to append to self.captured_packets
            # TODO: Use sniff() with stop_filter checking self.capturing
            pass

        # TODO: Create and start daemon thread
        # TODO: Sleep briefly to allow capture to start
        pass

    def stop_background_capture(self):
        """
        Stop background capture thread.
        """
        # TODO: Set self.capturing to False
        # TODO: Wait for thread to finish
        pass

    def send_ping_sequence(self, target_ip, count=5):
        """
        Send multiple ICMP ping packets.

        Args:
            target_ip: Target IP address
            count: Number of pings to send
        """
        # TODO: Loop count times
        # TODO: Create ICMP packet with incrementing ID
        # TODO: Send packet using send()
        # TODO: Store in self.sent_packets
        # TODO: Sleep between sends
        pass

    def send_port_scan(self, target_ip, ports):
        """
        Send TCP SYN packets to multiple ports.

        Args:
            target_ip: Target IP address
            ports: List of ports to scan
        """
        # TODO: Loop through ports
        # TODO: Create TCP SYN packet for each port
        # TODO: Send packet
        # TODO: Store in self.sent_packets
        pass

    def analyze_responses(self):
        """
        Correlate sent packets with captured responses.
        """
        # TODO: Loop through sent_packets
        # TODO: Find matching responses in captured_packets
        # TODO: Check for ICMP echo replies
        # TODO: Check for TCP responses (SYN-ACK, RST)
        # TODO: Print correlation statistics
        pass

    def generate_report(self):
        """
        Generate JSON report of traffic analysis.

        Returns:
            Dictionary with analysis results
        """
        report = {
            "sent_count": len(self.sent_packets),
            "captured_count": len(self.captured_packets),
            "protocols": {},
            "top_ips": {}
        }

        # TODO: Analyze captured packets
        # TODO: Count protocols
        # TODO: Count source IPs
        # TODO: Return report dictionary

        return report

    def save_results(self, base_filename="automation"):
        """
        Save packets and report to files.

        Args:
            base_filename: Base name for output files
        """
        # TODO: Save sent_packets to PCAP
        # TODO: Save captured_packets to PCAP
        # TODO: Generate report and save as JSON
        pass

def run_automated_test():
    """
    Execute automated packet testing sequence.
    """
    # TODO: Create PacketAutomation instance
    # TODO: Start background capture
    # TODO: Send ping sequence to 127.0.0.1
    # TODO: Send port scan to common ports
    # TODO: Wait for responses
    # TODO: Stop capture
    # TODO: Analyze responses
    # TODO: Generate and save report
    pass

def main():
    print("Starting automated packet operations")
    run_automated_test()
    print("Automation complete")

if __name__ == "__main__":
    main()
```

### 🔁 Step 4.2: Create Send-and-Receive Script

Create `send_receive.py`:

```python
#!/usr/bin/env python3
from scapy.all import *

def send_and_receive_icmp(target_ip, timeout=2):
    """
    Send ICMP packet and wait for response.

    Args:
        target_ip: Target IP address
        timeout: Response timeout in seconds

    Returns:
        Response packet or None
    """
    # TODO: Create ICMP echo request packet
    # TODO: Use sr1() to send and receive response
    # TODO: Check if response received
    # TODO: Return response packet
    pass

def send_and_receive_tcp(target_ip, target_port, timeout=2):
    """
    Send TCP SYN and wait for response.

    Args:
        target_ip: Target IP address
        target_port: Target port number
        timeout: Response timeout in seconds

    Returns:
        Response packet or None
    """
    # TODO: Create TCP SYN packet
    # TODO: Use sr1() to send and receive
    # TODO: Check response flags (SYN-ACK or RST)
    # TODO: Return response
    pass

def batch_send_receive(target_ip, ports):
    """
    Send packets to multiple ports and collect responses.

    Args:
        target_ip: Target IP address
        ports: List of ports to test

    Returns:
        Tuple of (answered, unanswered) packets
    """
    # TODO: Create list of TCP SYN packets for all ports
    # TODO: Use sr() to send all and collect responses
    # TODO: Return answered and unanswered packets
    pass

def main():
    target = "127.0.0.1"

    # TODO: Test ICMP send/receive
    # TODO: Test TCP send/receive on port 80
    # TODO: Test batch send/receive on ports [22, 80, 443]
    # TODO: Print results for each test

    print("Send/receive tests complete")

if __name__ == "__main__":
    main()
```

### ▶️ Step 4.3: Execute Automation Scripts

```bash
chmod +x packet_automation.py send_receive.py
sudo python3 packet_automation.py
sudo python3 send_receive.py
```

### 📊 Step 4.4: Review Generated Reports

```bash
# View PCAP files
ls -lh *.pcap

# View JSON report
cat automation_report_*.json | python3 -m json.tool
```

---

## 🛡️ Techniques & MITRE ATT&CK Reference

| Lab Technique | Concept | Related ATT&CK Technique | Tactic |
|---|---|---|---|
| TCP SYN Port Scanning | Active Scanning | [T1046 – Network Service Scanning](https://attack.mitre.org/techniques/T1046/) | Discovery |
| Custom Packet Crafting for Recon | IP Block Scanning | [T1595.001 – Active Scanning: Scanning IP Blocks](https://attack.mitre.org/techniques/T1595/001/) | Reconnaissance |
| Live Packet Capture / Sniffing | Traffic Interception | [T1040 – Network Sniffing](https://attack.mitre.org/techniques/T1040/) | Credential Access / Discovery |
| Raw ICMP/TCP Packet Crafting | Protocol-Level Covert Channel | [T1095 – Non-Application Layer Protocol](https://attack.mitre.org/techniques/T1095/) | Command and Control |
| DNS Query Capture & Analysis | DNS Traffic Abuse | [T1071.004 – Application Layer Protocol: DNS](https://attack.mitre.org/techniques/T1071/004/) | Command and Control |

---

## 🧯 Troubleshooting

<details>
<summary>🔴 Permission Denied Errors</summary>

- Always run Scapy scripts with `sudo` for raw socket access
- Check that your user has necessary network permissions

</details>

<details>
<summary>🟠 No Packets Captured</summary>

- Verify correct network interface name using `ip addr show`
- Generate test traffic in another terminal while capturing
- Check firewall rules: `sudo iptables -L`

</details>

<details>
<summary>🟡 Import Errors</summary>

- Ensure Scapy is installed: `pip3 list | grep scapy`
- Reinstall if needed: `sudo pip3 install --upgrade scapy`

</details>

<details>
<summary>🟢 Timeout Issues</summary>

- Increase timeout values in capture functions
- Use localhost (`127.0.0.1`) for testing to avoid network delays
- Check if target services are running: `netstat -tuln`

</details>

---

## ✅ Expected Outcomes

| Deliverable | Description |
|---|---|
| ⚙️ Scapy Setup | Successfully installed and configured Scapy |
| 🔨 Packet Crafting | Created scripts that craft various packet types (ICMP, TCP, UDP) |
| 📡 Live Capture | Captured live network traffic with filtering capabilities |
| 🔍 Protocol Analysis | Analyzed packet structures and protocol behaviors |
| 🤖 Automation | Automated packet operations with background capture |
| 📄 Reports | Generated PCAP files and analysis reports |

**Your scripts should demonstrate:**
- Proper packet layer construction
- Effective use of Scapy's sniffing functions
- Correlation between sent and received packets
- Statistical analysis of network traffic

---

## 📌 Key Takeaways

| Principle | Description |
|---|---|
| Programmatic Control | Scapy provides programmatic control over packet construction |
| Effective Filtering | Packet capture requires proper filtering for effective analysis |
| Systematic Testing | Automation enables systematic network testing and monitoring |
| Foundational Skill | Understanding packet structure is crucial for network security |

---

## 🚀 Next Steps

- Continue practicing by exploring additional protocols
- Implement custom packet analyzers
- Create more sophisticated automation workflows

---

<div align="center">

**Built with ❤️ for the next generation of cybersecurity professionals.**

</div>
