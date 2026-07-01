# 📊 Apply CVSS Scoring to Discovered Threats

<div align="center">

# 🚀 Apply CVSS Scoring to Discovered Threats
### Assess Vulnerabilities • Calculate Risk • Prioritize Remediation

<p align="center">

![Platform](https://img.shields.io/badge/Platform-Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CVSS](https://img.shields.io/badge/CVSS-v3.1-red?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-Processing-orange?style=for-the-badge)
![HTML](https://img.shields.io/badge/Reports-HTML-success?style=for-the-badge)
![CSV](https://img.shields.io/badge/Export-CSV-blue?style=for-the-badge)
![Risk](https://img.shields.io/badge/Risk-Assessment-purple?style=for-the-badge)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Vulnerability_Management-darkgreen?style=for-the-badge)

</p>

</div>

---

# 📖 Overview

Welcome to the **Apply CVSS Scoring to Discovered Threats** lab.

This hands-on cybersecurity lab introduces students to the **Common Vulnerability Scoring System (CVSS) v3.1**, the industry-standard framework for evaluating and communicating the severity of security vulnerabilities.

Throughout this lab, students will manually calculate CVSS scores, automate the scoring process using Python, generate professional vulnerability assessment reports, and prioritize discovered threats based on standardized severity ratings.

By combining vulnerability assessment with automation and reporting, learners will gain practical experience in communicating technical risk to both security professionals and management.

---

# 🎯 Lab Objectives

After completing this lab, you will be able to:

- ✅ Understand the CVSS v3.1 framework
- ✅ Interpret all CVSS Base Metrics
- ✅ Manually calculate CVSS Base Scores
- ✅ Build an automated Python CVSS calculator
- ✅ Generate CVSS Vector Strings
- ✅ Produce professional vulnerability reports
- ✅ Prioritize vulnerabilities using severity ratings
- ✅ Communicate security risk effectively

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python 3.8+ | Automation & scripting |
| 🐧 Linux | Development platform |
| 📄 JSON | Vulnerability datasets |
| 📊 CVSS v3.1 | Vulnerability scoring |
| 🌐 HTML | Executive reporting |
| 📑 CSV | Data export |
| 📋 File I/O | Report generation |
| 🔒 Vulnerability Assessment | Risk evaluation |

---

# 📚 What You Will Build

During this lab you will create:

- 📊 CVSS v3.1 Calculator
- 🧮 Manual scoring worksheet
- 🐍 Automated Python scoring engine
- 📄 JSON vulnerability processor
- 📈 Risk assessment reports
- 🌐 HTML executive reports
- 📑 CSV export reports
- 🎯 Vulnerability prioritization tool

---

# 🧩 Lab Workflow

---

# 🟢 Task 1 — Learn the CVSS Framework

## 🎯 Goal

Understand the components of CVSS v3.1 and prepare the assessment environment.

---

### ✔ Step 1.1 — Study CVSS Base Metrics

Learn the three major categories of CVSS metrics:

### 🔹 Exploitability Metrics

- 🌐 Attack Vector (AV)
- ⚙ Attack Complexity (AC)
- 🔑 Privileges Required (PR)
- 👤 User Interaction (UI)
- 🔄 Scope (S)

---

### 🔹 Impact Metrics

- 🔒 Confidentiality (C)
- ✔ Integrity (I)
- ⚡ Availability (A)

---

### 🔹 Severity Ratings

Understand severity classifications:

- ⚪ None
- 🟢 Low
- 🟡 Medium
- 🟠 High
- 🔴 Critical

---

### ✔ Step 1.2 — Create Lab Environment

Prepare the project by:

- 📁 Creating project directories
- 🐍 Preparing Python workspace
- 📂 Organizing scripts and reports

---

### ✔ Step 1.3 — Build Vulnerability Dataset

Create structured vulnerability data including:

- 🆔 Vulnerability IDs
- 📝 Descriptions
- 🔐 CVE identifiers
- 📊 CVSS metric values
- 🎯 Attack characteristics

Sample vulnerabilities include:

- 💉 SQL Injection
- 🌐 Stored XSS
- 🔓 Local Privilege Escalation

---

### ✔ Step 1.4 — Perform Manual CVSS Calculation

Practice calculating CVSS scores manually by:

- 🧮 Computing Exploitability Score
- 📈 Computing Impact Score
- 🎯 Determining Base Score
- 🚦 Assigning Severity Rating

---

# 🟡 Task 2 — Build the CVSS Calculator

## 🎯 Goal

Develop a Python application that automatically calculates CVSS scores.

---

### ✔ Step 2.1 — Implement CVSS Calculator

Create a reusable calculator capable of:

- 📊 Calculating Exploitability Score
- 📈 Calculating Impact Score
- 🎯 Computing Base Score
- 🚦 Determining Severity Rating
- 🏷 Generating CVSS Vector Strings
- 📄 Processing vulnerability datasets

---

### ✔ Step 2.2 — Test the Calculator

Validate your implementation by:

- ▶ Running the calculator
- 📊 Comparing generated scores
- ✔ Verifying severity ratings
- 🔍 Checking vector strings

---

### ✔ Step 2.3 — Build Report Generator

Develop a reporting engine capable of exporting:

- 📄 JSON Reports
- 🌐 HTML Reports
- 📑 CSV Reports

Include:

- 📊 Summary statistics
- 🚨 Severity distribution
- 🎯 Risk recommendations
- 📈 Vulnerability rankings

---

# 🔵 Task 3 — Generate Vulnerability Reports

## 🎯 Goal

Analyze multiple vulnerabilities and produce professional assessment reports.

---

### ✔ Step 3.1 — Create Additional Test Data

Expand the assessment by adding vulnerabilities such as:

- 💥 Remote Code Execution
- 🔍 Information Disclosure
- 🔐 Authentication Issues
- 🌐 Web Application Vulnerabilities

---

### ✔ Step 3.2 — Export Multiple Report Formats

Generate reports in:

- 📄 JSON
- 🌐 HTML
- 📑 CSV

Each report summarizes:

- CVSS Scores
- Severity Levels
- Vector Strings
- Risk Assessments

---

### ✔ Step 3.3 — Prioritize Vulnerabilities

Develop a prioritization engine that:

- 📈 Sorts by CVSS score
- 🚨 Groups by severity
- 📅 Assigns remediation timelines
- 🎯 Calculates overall organizational risk

---

### ✔ Step 3.4 — Create Executive Summary

Produce a management-ready report containing:

- 📊 Overall Risk Level
- 📈 Summary Statistics
- 🚨 Critical Findings
- 🎯 Top Priorities
- 🛡 Security Recommendations

---

# 📁 Project Structure

```text
cvss-lab/
│
├── vulnerabilities/
│   ├── sample_vulnerabilities.json
│   ├── web_vulnerabilities.json
│   └── manual_calculation.txt
│
├── scripts/
│   ├── cvss_calculator.py
│   ├── cvss_reporter.py
│   └── prioritize_vulns.py
│
└── reports/
    ├── report.json
    ├── report.html
    ├── report.csv
    └── executive_summary.txt
```

---

# 📊 Expected Outcomes

Upon successful completion you will have:

- ✅ Strong understanding of CVSS v3.1
- ✅ Manual CVSS calculation skills
- ✅ Automated Python scoring engine
- ✅ Professional vulnerability reports
- ✅ Executive security summaries
- ✅ Vulnerability prioritization framework
- ✅ Risk assessment automation
- ✅ Security reporting templates

---

# 📂 Generated Artifacts

| File | Description |
|------|-------------|
| 📄 sample_vulnerabilities.json | Sample vulnerability dataset |
| 📄 web_vulnerabilities.json | Additional vulnerability scenarios |
| 🐍 cvss_calculator.py | Automated CVSS calculator |
| 📊 cvss_reporter.py | Multi-format reporting engine |
| 📈 prioritize_vulns.py | Risk prioritization tool |
| 📄 report.json | JSON vulnerability report |
| 🌐 report.html | Executive HTML report |
| 📑 report.csv | CSV vulnerability report |
| 📋 executive_summary.txt | Management summary |

---

# 🎓 Skills You Will Gain

By completing this lab you will learn:

- 📊 CVSS v3.1 Methodology
- 🧮 Risk Scoring
- 🐍 Python Automation
- 📄 Vulnerability Reporting
- 📈 Security Metrics Analysis
- 🚨 Vulnerability Prioritization
- 📑 Executive Reporting
- 🔒 Risk Communication

---

# 💼 Real-World Applications

The knowledge gained in this lab is widely used in:

- 🛡 Vulnerability Management
- 🔍 Penetration Testing
- 📊 Risk Assessments
- 🏢 Security Operations Centers (SOC)
- 🚨 Incident Response
- 📋 Compliance Audits
- 🔐 Enterprise Security
- 🌐 Security Consulting

---

# ⚠️ Best Practices

- ✔ Always use the latest CVSS specification (v3.1).
- ✔ Validate manual calculations against trusted calculators.
- ✔ Maintain consistent vulnerability documentation.
- ✔ Prioritize remediation using both CVSS and business impact.
- ✔ Generate reports for both technical and executive audiences.
- ✔ Regularly update vulnerability datasets.

---

# 🎯 Learning Outcomes

By the end of this lab, students will confidently be able to:

✅ Interpret all CVSS v3.1 metrics

✅ Calculate CVSS Base Scores manually

✅ Automate vulnerability scoring with Python

✅ Generate CVSS vector strings

✅ Produce professional vulnerability reports

✅ Prioritize remediation using standardized severity ratings

✅ Communicate technical security risks to stakeholders

---

# 📚 Conclusion

The **Apply CVSS Scoring to Discovered Threats** lab provides practical experience with the industry-standard **CVSS v3.1** framework for vulnerability assessment. Students learn how to quantify security risks through manual calculations, automate scoring using Python, and generate professional reports suitable for both technical teams and executive leadership.

These skills are essential for vulnerability management, penetration testing, compliance assessments, and enterprise risk management, enabling organizations to make informed, risk-based remediation decisions.

---

# 🔑 Key Takeaways

- 📊 CVSS provides a standardized method for evaluating vulnerability severity.
- 🧮 Manual calculations strengthen understanding of CVSS metrics and formulas.
- 🐍 Automation increases efficiency, accuracy, and consistency.
- 📈 Risk prioritization enables effective remediation planning.
- 📄 Professional reporting supports technical teams and executive stakeholders.
- 🎯 Standardized scoring improves vulnerability management across organizations.
- 🔒 Quantitative risk assessments drive better cybersecurity decisions.

---

<div align="center">

## 📊 Happy Vulnerability Scoring!

**Assess • Score • Prioritize • Protect**

⭐ **Transform Vulnerability Data into Actionable Security Intelligence**

</div>
