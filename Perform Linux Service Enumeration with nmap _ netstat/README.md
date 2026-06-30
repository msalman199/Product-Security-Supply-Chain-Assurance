# 🛰️ Perform Linux Service Enumeration with nmap & netstat

> **Product Security & Supply Chain Assurance (PSSCA) Lab**

![Linux](https://img.shields.io/badge/Linux-Ubuntu%2020.04+-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Nmap](https://img.shields.io/badge/Nmap-Network%20Scanner-00457C?style=for-the-badge&logo=nmap&logoColor=white)
![Netstat](https://img.shields.io/badge/Netstat-Network%20Analysis-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=yellow)
![Bash](https://img.shields.io/badge/Bash-Scripting-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Service%20Enumeration-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-success?style=for-the-badge)

---

# 📖 Overview

Service enumeration is one of the most important phases of **Product Security Assessment**, **Infrastructure Security**, and **Supply Chain Assurance**.

This lab teaches students how to identify exposed services, discover listening ports, analyze active network connections, and automate reconnaissance using industry-standard open-source tools.

Students will combine **Nmap**, **Netstat**, **Python**, and **Bash scripting** to create automated enumeration frameworks capable of generating professional security reports.

---

# 🎯 Learning Objectives

After completing this lab, you will be able to:

- ✅ Understand Linux service enumeration fundamentals
- ✅ Discover open ports using Nmap
- ✅ Detect running services and versions
- ✅ Identify listening ports using Netstat
- ✅ Analyze active TCP and UDP connections
- ✅ Automate enumeration using Python
- ✅ Build reusable Bash automation scripts
- ✅ Generate structured security reports
- ✅ Interpret enumeration results for security assessments
- ✅ Apply reconnaissance techniques in Product Security engagements

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐧 Ubuntu Linux | Operating System |
| 🌐 Nmap | Network & Service Scanner |
| 📡 Netstat | Network Connection Monitoring |
| 🐍 Python 3 | Automation |
| 💻 Bash | Automation Scripts |
| 📄 JSON | Report Generation |
| 📊 Text Reports | Documentation |

---

# 📚 Lab Prerequisites

Before starting this lab you should understand:

- Linux command line
- TCP/IP networking
- Ports and protocols
- Common network services
- Python basics
- Bash scripting
- Cybersecurity fundamentals

---

# 🖥 Lab Environment

The cloud machine includes:

- Ubuntu 20.04+
- Python 3
- Nmap
- Netstat
- Bash
- Internet connectivity
- Preconfigured lab environment

---

# 📂 Lab Structure

```
service-enumeration/
│
├── nmap_scan.sh
├── netstat_monitor.sh
├── service_enumeration.py
├── advanced_nmap_scripts.py
├── analyze_services.py
├── master_enumeration.sh
│
├── scan_results/
├── netstat_results/
├── enumeration_results/
└── reports/
```

---

# 🚩 Task 1 — Enumerate Services Using Nmap

## 🎯 Objective

Learn how to discover:

- Open ports
- Running services
- Service versions
- Operating system information
- Network exposure

---

## ✅ Step 1 — Install Nmap

Verify installation.

Skills learned:

- Installing packages
- Version verification
- Tool validation

---

## ✅ Step 2 — Perform Basic Port Scanning

Students perform:

- Localhost scan
- Custom port scan
- Full TCP scan

Concepts:

- TCP Ports
- Open vs Closed ports
- Service Discovery

---

## ✅ Step 3 — Service Version Detection

Students use:

- Service fingerprinting
- OS detection
- NSE scripts

Topics covered:

- Banner grabbing
- Version identification
- Security reconnaissance

---

## ✅ Step 4 — Create Bash Automation

Students build:

```
nmap_scan.sh
```

Features:

- Automatic scans
- Organized output
- Multiple scan types
- Report generation

---

# 🚩 Task 2 — Analyze Active Connections Using Netstat

## 🎯 Objective

Understand live network activity.

---

## ✅ Step 1 — Install Netstat

Verify installation using:

- net-tools
- version checking

---

## ✅ Step 2 — Identify Listening Ports

Students learn:

- TCP listeners
- UDP listeners
- Process ownership
- Numerical addresses

---

## ✅ Step 3 — Analyze Active Connections

Students inspect:

- Established sessions
- Routing tables
- Network statistics
- Connected hosts

---

## ✅ Step 4 — Automate Monitoring

Students create

```
netstat_monitor.sh
```

Features:

- Timestamped reports
- Listening services
- Active connections
- Statistics
- Summary generation

---

# 🚩 Task 3 — Automate Enumeration Using Python

## 🎯 Objective

Create reusable enumeration tools.

---

## ✅ Step 1 — Install Python Dependencies

Students install:

- python3-pip
- python-nmap

Purpose:

Enable Python automation.

---

## ✅ Step 2 — Build Service Enumerator

Students create

```
service_enumeration.py
```

Capabilities:

- TCP scanning
- Service detection
- Netstat parsing
- JSON reports
- Text reports

---

## ✅ Step 3 — Advanced Nmap Automation

Students develop

```
advanced_nmap_scripts.py
```

Capabilities include:

- Vulnerability scanning
- Banner detection
- Service fingerprinting
- Stealth scanning
- Comprehensive scans

---

## ✅ Step 4 — Execute Automation

Students perform:

- Python execution
- Report generation
- Scan validation

---

## ✅ Step 5 — Create Master Automation Script

Students build

```
master_enumeration.sh
```

Workflow:

1. Nmap Scan
2. Netstat Analysis
3. Python Automation
4. Report Generation
5. Summary Creation

---

# 🚩 Task 4 — Analyze Results

## 🎯 Objective

Interpret enumeration findings.

Students compare:

- Nmap results
- Netstat output
- Open services
- Active sessions
- Running processes

---

## ✅ Service Identification

Students identify services including:

- SSH
- HTTP
- HTTPS
- FTP
- SMTP
- DNS
- MySQL
- PostgreSQL
- Redis
- MongoDB

---

## ✅ Security Analysis

Students determine:

- Unnecessary services
- Weak protocols
- Legacy software
- Exposed databases
- Public attack surface

---

# 🤖 Python Automation Features

The lab includes automation for:

✅ TCP Enumeration

✅ Service Detection

✅ Version Detection

✅ JSON Reporting

✅ Text Reporting

✅ Port Classification

✅ Active Connection Analysis

✅ Service Categorization

---

# 📊 Reports Generated

The automation produces:

```
enumeration_report.json

enumeration_report.txt

master_summary.txt

basic_scan.txt

service_scan.txt

aggressive_scan.txt

udp_scan.txt

script_scan.txt

network_stats.txt
```

---

# 📈 Skills Gained

Students gain experience in:

- Linux Enumeration
- Port Scanning
- Network Reconnaissance
- Service Discovery
- Network Monitoring
- Bash Automation
- Python Automation
- Report Writing
- Security Documentation

---

# 🔒 Security Concepts Covered

- Attack Surface Enumeration
- Service Fingerprinting
- Network Visibility
- Banner Grabbing
- Active Connection Analysis
- Open Port Discovery
- Enumeration Automation
- Infrastructure Assessment

---

# 🧠 Best Practices

✔ Enumerate only authorized systems

✔ Verify discovered services

✔ Document findings

✔ Remove unnecessary services

✔ Monitor exposed ports

✔ Automate repetitive tasks

✔ Secure generated reports

✔ Keep scanning tools updated

---

# ⚠ Common Troubleshooting

## Nmap Not Installed

- Install via package manager
- Verify version
- Confirm executable path

---

## Netstat Missing

Install:

- net-tools

Verify installation before continuing.

---

## Permission Errors

Use elevated privileges when required for:

- SYN scans
- Process enumeration

---

## Python Module Errors

Install:

- python-nmap
- pip dependencies

---

## Slow Scans

Use:

- Timing templates
- Targeted scans
- Specific port ranges

---

# 🎓 Learning Outcomes

Upon successful completion, students will be able to:

- Perform Linux service enumeration
- Identify exposed services
- Detect active network connections
- Automate reconnaissance workflows
- Create reusable security tools
- Generate professional reports
- Analyze service exposure
- Conduct infrastructure reconnaissance
- Support Product Security assessments
- Improve organizational security posture

---

# 🌍 Real-World Applications

These techniques are widely used in:

- Product Security
- Supply Chain Assurance
- Infrastructure Security
- Penetration Testing
- Red Team Operations
- Blue Team Monitoring
- Security Auditing
- Compliance Assessments
- DevSecOps
- Incident Response

---

# 🏆 Key Takeaways

✔ Nmap is the industry standard for service enumeration.

✔ Netstat provides real-time network visibility.

✔ Combining multiple tools improves reconnaissance accuracy.

✔ Python enables scalable security automation.

✔ Bash scripting streamlines repetitive tasks.

✔ Structured reporting improves security documentation.

✔ Enumeration is a foundational step in every security assessment.

✔ Automation enhances consistency, efficiency, and repeatability.

---

# 📚 Conclusion

In this lab, you developed practical skills in Linux service enumeration using **Nmap**, **Netstat**, **Python**, and **Bash**. You learned how to identify exposed services, analyze network activity, automate reconnaissance workflows, and generate professional security reports.

These techniques are essential for **Product Security & Supply Chain Assurance**, enabling security professionals to assess system exposure, validate configurations, identify unnecessary services, and support secure infrastructure deployments. The automation scripts created throughout this lab provide a reusable foundation for future penetration testing, security auditing, and enterprise-scale network assessments.

---

## 👨‍💻 Happy Learning & Happy Hacking! 🚀
**Product Security & Supply Chain Assurance (PSSCA)**
