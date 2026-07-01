<div align="center">

# 🔗 Analyze Update Mechanisms for Supply Chain Risks

### Package Manager, Network Traffic & TLS Security Assessment Lab

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04_LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![APT](https://img.shields.io/badge/APT-Package_Manager-A80030?style=for-the-badge&logo=debian&logoColor=white)
![pip](https://img.shields.io/badge/pip-Package_Manager-3775A9?style=for-the-badge&logo=pypi&logoColor=white)
![TLS/SSL](https://img.shields.io/badge/TLS%2FSSL-Security_Analysis-0052CC?style=for-the-badge&logo=letsencrypt&logoColor=white)
![tcpdump](https://img.shields.io/badge/tcpdump-Traffic_Capture-14354C?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Supply_Chain_Security-CC0000?style=for-the-badge)

</div>

---

> ⚠️ **AUTHORIZED USE ONLY**
> This lab is intended strictly for **educational purposes** within the Al Nafi training environment. Only scan, monitor, or evaluate infrastructure you own or are explicitly authorized to test. Do not run network monitoring or TLS assessment tools against third-party or production systems without written authorization.

---

## 📑 Table of Contents

- [🧰 Technology Stack](#-technology-stack)
- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment](#️-lab-environment)
- [📁 Directory Structure](#-directory-structure)
- [🔄 Audit Workflow](#-audit-workflow)
- [📦 Task 1: Audit Package Manager Security](#-task-1-audit-package-manager-security)
- [📡 Task 2: Monitor Update Network Traffic](#-task-2-monitor-update-network-traffic)
- [🔐 Task 3: Evaluate TLS Security of Update Servers](#-task-3-evaluate-tls-security-of-update-servers)
- [🧩 Task 4: Create Comprehensive Supply Chain Auditor](#-task-4-create-comprehensive-supply-chain-auditor)
- [🛡️ Vulnerability & MITRE ATT&CK Reference](#️-vulnerability--mitre-attck-reference)
- [🧯 Troubleshooting](#-troubleshooting)
- [✅ Expected Outcomes](#-expected-outcomes)
- [📌 Key Takeaways](#-key-takeaways)
- [🚀 Next Steps](#-next-steps)

---

## 🧰 Technology Stack

| Technology | Purpose | Badge |
|---|---|---|
| **Python 3.10+** | Core scripting language for all analysis tools | ![Python](https://img.shields.io/badge/Python-Automation-3776AB?style=flat-square&logo=python&logoColor=white) |
| **APT** | Debian/Ubuntu package manager under audit | ![APT](https://img.shields.io/badge/APT-Debian_Pkg_Mgr-A80030?style=flat-square&logo=debian&logoColor=white) |
| **pip** | Python package manager under audit | ![pip](https://img.shields.io/badge/pip-Python_Pkg_Mgr-3775A9?style=flat-square&logo=pypi&logoColor=white) |
| **ssl / socket** | Python modules for TLS handshake and certificate inspection | ![TLS](https://img.shields.io/badge/TLS-Cert_Inspection-0052CC?style=flat-square) |
| **tcpdump / netstat** | Native network traffic and connection state visibility | ![Networking](https://img.shields.io/badge/Networking-Traffic_Analysis-14354C?style=flat-square) |
| **Ubuntu 22.04 LTS** | Target operating system and cloud lab base image | ![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04_LTS-E95420?style=flat-square&logo=ubuntu&logoColor=white) |

---

## 🎯 Objectives

| # | Objective |
|---|---|
| 1 | Identify vulnerabilities in software update mechanisms |
| 2 | Analyze package manager configurations for security risks |
| 3 | Evaluate TLS/SSL security of update servers |
| 4 | Monitor network traffic during update processes |
| 5 | Create automated tools to assess supply chain security |

---

## 📋 Prerequisites

| # | Requirement |
|---|---|
| 1 | Basic Linux command line proficiency |
| 2 | Understanding of networking concepts (HTTP/HTTPS, DNS, TLS) |
| 3 | Python programming fundamentals |
| 4 | Familiarity with package managers (apt, pip) |

---

## 🖥️ Lab Environment

> 💡 Al Nafi provides pre-configured Linux cloud machines. Click **Start Lab** to access your environment with:

| Component | Version / Tooling |
|---|---|
| OS | Ubuntu 22.04 LTS |
| Runtime | Python 3.10+ |
| Network Tools | `tcpdump`, `netstat` |
| Editors | `nano`, `vim` |

---

## 📁 Directory Structure

```
supply-chain-lab/
├── package_analyzer.py          # APT & pip configuration security analyzer
├── update_monitor.py            # Network traffic monitor during updates
├── tls_analyzer.py               # TLS/SSL security evaluator
├── supply_chain_auditor.py       # Integrated audit framework
└── reports/
    ├── package_security_report.json
    ├── traffic_report.json
    ├── tls_report.json
    └── audit_report.json
```

---

## 🔄 Audit Workflow

```
        ┌───────────────────────┐
        │   Package Manager       │
        │   (APT / pip configs)   │
        └───────────┬─────────────┘
                    │  analyze
                    ▼
        ┌───────────────────────┐
        │  package_analyzer.py    │──► package_security_report.json
        └───────────┬─────────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │   Live Update Traffic    │
        │   (netstat / tcpdump)   │
        └───────────┬─────────────┘
                    │  capture
                    ▼
        ┌───────────────────────┐
        │  update_monitor.py       │──► traffic_report.json
        └───────────┬─────────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │   Update Servers          │
        │  (archive.ubuntu.com,    │
        │   pypi.org, github.com)  │
        └───────────┬─────────────┘
                    │  TLS handshake
                    ▼
        ┌───────────────────────┐
        │  tls_analyzer.py          │──► tls_report.json
        └───────────┬─────────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │ supply_chain_auditor.py  │──► audit_report.json
        │  (weighted risk score)   │      + risk_level
        └───────────────────────┘
```

---

## 📦 Task 1: Audit Package Manager Security

### 📖 Overview

Package managers are critical components in the software supply chain. Insecure configurations can expose systems to man-in-the-middle attacks, malicious packages, and compromised updates.

### 📂 Step 1: Create Working Directory

```bash
mkdir ~/supply-chain-lab
cd ~/supply-chain-lab
```

### 🔍 Step 2: Examine APT Configuration

```bash
# View APT sources
cat /etc/apt/sources.list
ls -la /etc/apt/sources.list.d/

# Check GPG keys
apt-key list
```

**🔑 Key Security Indicators:**
- HTTP vs HTTPS sources
- Trusted GPG keys
- Third-party repositories

### 🛠️ Step 3: Build Package Security Analyzer

Create `package_analyzer.py`:

```python
#!/usr/bin/env python3
"""
Package Manager Security Analyzer
Students: Complete the TODOs to analyze package manager security
"""

import os
import re
import json

class PackageSecurityAnalyzer:
    def __init__(self):
        self.vulnerabilities = []
        self.security_score = 100

    def analyze_apt_sources(self):
        """Analyze APT sources for security issues"""
        print("=== Analyzing APT Sources ===")

        sources_files = ['/etc/apt/sources.list']
        sources_dir = '/etc/apt/sources.list.d/'

        # TODO: Add logic to find all .list files in sources_dir
        # TODO: Iterate through each source file
        # TODO: Check for HTTP (non-HTTPS) sources
        # TODO: Identify suspicious domains or IP addresses
        # TODO: Add findings to self.vulnerabilities list

        pass

    def check_source_line(self, filepath, line_num, line):
        """Check individual source line for security issues"""

        # TODO: Detect HTTP sources (not HTTPS)
        # TODO: Check for IP addresses instead of domain names
        # TODO: Identify suspicious TLDs (.tk, .ml, .ga)
        # TODO: Return issue dictionary with severity level

        pass

    def analyze_pip_config(self):
        """Analyze pip configuration for security risks"""
        print("\n=== Analyzing Pip Configuration ===")

        config_paths = [
            os.path.expanduser('~/.pip/pip.conf'),
            '/etc/pip.conf'
        ]

        # TODO: Check each config file for existence
        # TODO: Parse configuration for index-url settings
        # TODO: Identify HTTP index URLs
        # TODO: Check for trusted-host entries (SSL bypass)

        pass

    def calculate_risk_score(self):
        """Calculate overall security risk score"""

        # TODO: Implement scoring algorithm
        # TODO: Deduct points for HIGH severity issues (20 points)
        # TODO: Deduct points for MEDIUM severity issues (10 points)
        # TODO: Deduct points for LOW severity issues (5 points)
        # TODO: Return final score (0-100)

        pass

    def generate_report(self):
        """Generate security assessment report"""

        # TODO: Group vulnerabilities by severity
        # TODO: Print summary statistics
        # TODO: Save detailed report to JSON file
        # TODO: Provide remediation recommendations

        pass

def main():
    analyzer = PackageSecurityAnalyzer()
    analyzer.analyze_apt_sources()
    analyzer.analyze_pip_config()
    analyzer.calculate_risk_score()
    analyzer.generate_report()

if __name__ == "__main__":
    main()
```

### ▶️ Step 4: Run the Analyzer

```bash
chmod +x package_analyzer.py
python3 package_analyzer.py
```

**🎯 Expected Findings:**
- HTTP sources (HIGH risk)
- Missing GPG verification
- Untrusted repositories

---

## 📡 Task 2: Monitor Update Network Traffic

### 📖 Overview

Network traffic analysis during updates reveals potential security issues like unencrypted connections, suspicious destinations, and certificate problems.

### 🛠️ Step 1: Create Network Monitor

Create `update_monitor.py`:

```python
#!/usr/bin/env python3
"""
Update Network Traffic Monitor
Students: Complete the implementation to monitor update traffic
"""

import subprocess
import json
import time
import threading
from datetime import datetime

class UpdateNetworkMonitor:
    def __init__(self):
        self.connections = []
        self.monitoring = False
        self.suspicious_activity = []

    def start_monitoring(self):
        """Start network traffic monitoring"""

        # TODO: Set monitoring flag to True
        # TODO: Create thread for connection monitoring
        # TODO: Start the monitoring thread

        pass

    def monitor_connections(self):
        """Monitor active network connections"""

        while self.monitoring:
            # TODO: Execute netstat command to get connections
            # TODO: Parse output for ESTABLISHED connections
            # TODO: Store connection details with timestamp
            # TODO: Sleep for 2 seconds between checks

            pass

    def analyze_connection(self, connection):
        """Analyze individual connection for security issues"""

        # TODO: Check if connection uses port 80 (HTTP)
        # TODO: Identify connections to IP addresses vs domains
        # TODO: Flag suspicious ports (1337, 4444, etc.)
        # TODO: Return security assessment

        pass

    def simulate_update(self):
        """Simulate package update process"""

        # TODO: Start network monitoring
        # TODO: Execute apt list --upgradable
        # TODO: Wait for traffic capture
        # TODO: Stop monitoring
        # TODO: Analyze captured connections

        pass

    def generate_traffic_report(self):
        """Generate network traffic analysis report"""

        # TODO: Summarize total connections captured
        # TODO: List unique destinations
        # TODO: Highlight security issues found
        # TODO: Save report to JSON file

        pass

def main():
    monitor = UpdateNetworkMonitor()
    monitor.simulate_update()
    monitor.generate_traffic_report()

if __name__ == "__main__":
    main()
```

### ▶️ Step 2: Execute Network Monitoring

```bash
python3 update_monitor.py
```

### 📊 Step 3: Analyze Results

Review the generated report for:
- Unencrypted HTTP connections
- Unknown destination servers
- Suspicious port usage
- Connection patterns

---

## 🔐 Task 3: Evaluate TLS Security of Update Servers

### 📖 Overview

TLS/SSL security is critical for protecting update downloads from tampering. This task analyzes certificate validity, cipher strength, and protocol versions.

### 🛠️ Step 1: Create TLS Analyzer

Create `tls_analyzer.py`:

```python
#!/usr/bin/env python3
"""
TLS Security Analyzer for Update Servers
Students: Implement TLS security checks
"""

import ssl
import socket
from datetime import datetime

class TLSSecurityAnalyzer:
    def __init__(self):
        self.results = []
        self.update_servers = [
            'archive.ubuntu.com',
            'security.ubuntu.com',
            'pypi.org',
            'github.com'
        ]

    def analyze_server(self, hostname, port=443):
        """Analyze TLS configuration of update server"""

        # TODO: Create SSL context
        # TODO: Connect to server and retrieve certificate
        # TODO: Extract certificate details (expiry, issuer, etc.)
        # TODO: Get TLS version and cipher suite
        # TODO: Return analysis results

        pass

    def check_certificate_expiry(self, cert):
        """Check certificate expiration date"""

        # TODO: Parse notAfter date from certificate
        # TODO: Calculate days until expiration
        # TODO: Flag certificates expiring within 30 days
        # TODO: Return expiry status

        pass

    def evaluate_tls_version(self, version):
        """Evaluate TLS protocol version security"""

        # TODO: Check if TLS version is 1.2 or higher
        # TODO: Flag TLSv1.0 and TLSv1.1 as insecure
        # TODO: Return security assessment

        pass

    def evaluate_cipher_suite(self, cipher):
        """Evaluate cipher suite strength"""

        # TODO: Check for weak ciphers (RC4, DES, 3DES)
        # TODO: Verify key length (minimum 128-bit)
        # TODO: Check for forward secrecy support
        # TODO: Return cipher security rating

        pass

    def analyze_all_servers(self):
        """Analyze all configured update servers"""

        # TODO: Iterate through self.update_servers
        # TODO: Call analyze_server for each
        # TODO: Collect and store results
        # TODO: Handle connection errors gracefully

        pass

    def generate_tls_report(self):
        """Generate comprehensive TLS security report"""

        # TODO: Summarize servers analyzed
        # TODO: List HIGH severity issues
        # TODO: List MEDIUM severity issues
        # TODO: Provide remediation recommendations
        # TODO: Save report to JSON file

        pass

def main():
    analyzer = TLSSecurityAnalyzer()
    analyzer.analyze_all_servers()
    analyzer.generate_tls_report()

if __name__ == "__main__":
    main()
```

### ▶️ Step 2: Run TLS Analysis

```bash
python3 tls_analyzer.py
```

### 📊 Step 3: Review TLS Security

Examine the report for:
- Certificate expiration warnings
- Weak TLS versions (< 1.2)
- Insecure cipher suites
- Certificate chain issues

---

## 🧩 Task 4: Create Comprehensive Supply Chain Auditor

### 📖 Overview

Integrate all previous analyses into a unified auditing framework that provides an overall security assessment.

### 🛠️ Step 1: Build Integrated Auditor

Create `supply_chain_auditor.py`:

```python
#!/usr/bin/env python3
"""
Comprehensive Supply Chain Security Auditor
Students: Integrate all security checks into unified framework
"""

import json
from datetime import datetime

class SupplyChainAuditor:
    def __init__(self):
        self.audit_results = {
            'timestamp': datetime.now().isoformat(),
            'package_security': {},
            'network_security': {},
            'tls_security': {},
            'overall_score': 0,
            'risk_level': 'UNKNOWN'
        }

    def run_full_audit(self):
        """Execute comprehensive security audit"""

        # TODO: Run package manager security checks
        # TODO: Execute network traffic analysis
        # TODO: Perform TLS security evaluation
        # TODO: Aggregate all results

        pass

    def calculate_overall_score(self):
        """Calculate overall security score"""

        # TODO: Weight different security categories
        # TODO: Package security: 40%
        # TODO: Network security: 30%
        # TODO: TLS security: 30%
        # TODO: Calculate weighted average

        pass

    def determine_risk_level(self, score):
        """Determine risk level based on score"""

        # TODO: Score >= 90: LOW risk
        # TODO: Score 70-89: MEDIUM risk
        # TODO: Score 50-69: HIGH risk
        # TODO: Score < 50: CRITICAL risk

        pass

    def generate_recommendations(self):
        """Generate security recommendations"""

        # TODO: Analyze all findings
        # TODO: Prioritize by severity
        # TODO: Provide specific remediation steps
        # TODO: Include best practices

        pass

    def export_audit_report(self):
        """Export comprehensive audit report"""

        # TODO: Format results for readability
        # TODO: Include executive summary
        # TODO: Detail all findings by category
        # TODO: Save to JSON and text formats

        pass

def main():
    auditor = SupplyChainAuditor()
    auditor.run_full_audit()
    auditor.calculate_overall_score()
    auditor.generate_recommendations()
    auditor.export_audit_report()

    print("\nAudit complete! Review the generated reports.")

if __name__ == "__main__":
    main()
```

### ▶️ Step 2: Execute Full Audit

```bash
python3 supply_chain_auditor.py
```

### 📊 Step 3: Review Audit Results

Examine the comprehensive report for:
- Overall security score
- Risk level classification
- Prioritized vulnerabilities
- Remediation recommendations

---

## 🛡️ Vulnerability & MITRE ATT&CK Reference

| Risk | CWE ID | Related ATT&CK Technique | Tactic |
|---|---|---|---|
| Unsigned / Unverified Package Downloads | CWE-494 | [T1195.002 – Compromise Software Supply Chain](https://attack.mitre.org/techniques/T1195/002/) | Initial Access |
| Compromised Dependency or Repository | CWE-829 | [T1195.001 – Compromise Software Dependencies and Development Tools](https://attack.mitre.org/techniques/T1195/001/) | Initial Access |
| HTTP (Unencrypted) Update Channel | CWE-319 | [T1557 – Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557/) | Collection / Credential Access |
| Missing or Improper Certificate Validation | CWE-295 | [T1553.004 – Subvert Trust Controls: Install Root Certificate](https://attack.mitre.org/techniques/T1553/004/) | Defense Evasion |
| Weak / Deprecated TLS Version or Cipher | CWE-326 | [T1040 – Network Sniffing](https://attack.mitre.org/techniques/T1040/) | Credential Access / Discovery |

---

## 🧯 Troubleshooting

<details>
<summary>🔴 Permission Denied Reading System Files</summary>

Use `sudo` for system configuration files or run scripts with elevated privileges.

</details>

<details>
<summary>🟠 Network Monitoring Shows No Connections</summary>

Ensure network activity is occurring; try `sudo apt update` in another terminal.

</details>

<details>
<summary>🟡 TLS Connection Timeouts</summary>

Check firewall settings; verify internet connectivity; some servers may block automated connections.

</details>

<details>
<summary>🟢 Python Module Import Errors</summary>

Install required modules: `pip3 install --user <module_name>`

</details>

---

## ✅ Expected Outcomes

| Deliverable | Description |
|---|---|
| 📦 Package Security Analysis | Identified common vulnerabilities in update mechanisms |
| 🤖 Automated Tools | Created automated tools for security assessment |
| 📡 Network Traffic Data | Analyzed network traffic during update processes |
| 🔐 TLS Security Assessment | Evaluated TLS/SSL security of update servers |
| 📄 Audit Report | Generated comprehensive security audit reports |
| 🧠 Applied Skills | Developed practical skills in supply chain security analysis |

**Key Deliverables:**
- Package security analysis report
- Network traffic monitoring data
- TLS security assessment
- Integrated audit report with recommendations

---

## 📌 Key Takeaways

| Principle | Description |
|---|---|
| Attack Surface | Update mechanisms are critical attack vectors in supply chains |
| Automation | Automated analysis tools improve security assessment efficiency |
| Defense in Depth | Multiple layers of security (package signing, TLS, network monitoring) are necessary |
| Continuous Assurance | Regular audits help maintain supply chain integrity |

---

## 🚀 Next Steps

- Implement automated monitoring in production environments
- Integrate findings into CI/CD pipelines
- Develop organizational policies for update security
- Stay informed about emerging supply chain threats

---

<div align="center">

**Built with ❤️ for the next generation of cybersecurity professionals.**

</div>
