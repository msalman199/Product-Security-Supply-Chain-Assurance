# 📱 Enumerate Android Apps with apktool, JADX, and apkleaks

> **Learn how to perform static security analysis of Android applications by decompiling APKs, reviewing source code, extracting sensitive information, automating security assessments, and generating professional vulnerability reports using apktool, JADX, apkleaks, and Python.**

---

# 🎯 Purpose of this Lab

This lab is designed to provide hands-on experience in **Android Application Security Assessment** through static analysis techniques. Students will learn how to reverse engineer Android applications, inspect application resources, analyze source code, discover security weaknesses, and identify sensitive information embedded within APK files.

Throughout the lab, participants will use **apktool** to decompile Android packages, **JADX** to convert DEX bytecode into readable Java source code, and **apkleaks** to automatically detect hardcoded credentials, API keys, tokens, and other sensitive data. In addition, learners will develop Python automation scripts that streamline APK analysis, improve assessment efficiency, and generate professional security reports.

By combining multiple industry-standard tools, this lab demonstrates the complete workflow used by mobile application security engineers, penetration testers, malware analysts, reverse engineers, and security researchers when performing Android application assessments.

---

# 🚀 Learning Objectives

After completing this lab, you will be able to:

- 📦 Decompile Android APK files
- 📄 Extract AndroidManifest.xml and application resources
- 💻 Analyze decompiled Java source code
- 🔍 Detect hardcoded credentials and secrets
- 🔐 Identify insecure application configurations
- ⚠️ Discover common Android security vulnerabilities
- 🐍 Automate APK security assessments using Python
- 📊 Generate professional security assessment reports
- 📱 Perform comprehensive static application security testing
- 🛡️ Improve Android application security posture

---

# 🧠 Skills You Will Gain

- Android Reverse Engineering
- Static Application Security Testing (SAST)
- Mobile Application Security
- Android Manifest Analysis
- Source Code Review
- Secret Discovery
- Security Automation
- Python Scripting
- Vulnerability Identification
- Security Reporting

---

# 🔬 What You Will Build

During this lab you will create:

- 🐍 APK decompilation automation scripts
- 🔍 Java source code analyzers
- 🔑 Secret detection utilities
- 📊 Comprehensive APK analysis frameworks
- 📄 HTML security report generators
- 📑 JSON assessment reports
- ⚙️ Batch APK analysis tools
- 🛡️ Automated mobile security assessment pipelines

---

# 🛠️ Technologies Used

<p align="center">

![Android](https://img.shields.io/badge/Android-3DDC84?logo=android&logoColor=white)
![APK](https://img.shields.io/badge/APK-Analysis-green)
![Java](https://img.shields.io/badge/Java-ED8B00?logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?logo=json)
![HTML](https://img.shields.io/badge/HTML-Reports-orange?logo=html5)

</p>

---

# 🔧 Security Tools

<p align="center">

![apktool](https://img.shields.io/badge/apktool-Decompiler-success)
![JADX](https://img.shields.io/badge/JADX-Java%20Decompiler-blue)
![apkleaks](https://img.shields.io/badge/apkleaks-Secret%20Scanner-red)
![Python](https://img.shields.io/badge/Python-Automation-3776AB?logo=python)
![grep](https://img.shields.io/badge/grep-Pattern%20Matching-lightgrey)
![jq](https://img.shields.io/badge/jq-JSON%20Processor-40A02B)

</p>

---

# 📚 Topics Covered

- 📱 Android APK Structure
- 📦 APK Decompilation
- 📄 AndroidManifest.xml Analysis
- 💻 Java Source Code Review
- 🔍 Static Application Security Testing (SAST)
- 🔐 Hardcoded Secret Detection
- 🌐 API Key Discovery
- 🔑 Credential Extraction
- ⚠️ Android Security Misconfigurations
- 🛡️ Mobile Application Security
- 🐍 Python Security Automation
- 📊 Security Report Generation
- 📑 JSON Reporting
- 📄 HTML Report Generation

---

# 🧪 Hands-on Exercises

This lab includes practical exercises such as:

- ✅ Decompiling APKs using apktool
- ✅ Exploring AndroidManifest.xml
- ✅ Reviewing application resources
- ✅ Decompiling Java source with JADX
- ✅ Searching for hardcoded credentials
- ✅ Identifying SQL Injection risks
- ✅ Detecting insecure HTTP communications
- ✅ Reviewing WebView configurations
- ✅ Running apkleaks secret scans
- ✅ Creating custom secret detection patterns
- ✅ Building Python automation tools
- ✅ Generating HTML security reports
- ✅ Performing batch APK analysis

---

# 🔍 Security Issues You Will Identify

Throughout this lab you will learn to identify:

- 🔑 Hardcoded API Keys
- 🔐 Embedded Passwords
- 🎫 Authentication Tokens
- ☁️ Cloud Service Credentials
- 🌐 Insecure HTTP Connections
- ⚠️ Debug Mode Enabled
- 📤 Exported Android Components
- 💉 SQL Injection Risks
- 🔒 Weak Cryptographic Implementations
- 📱 Insecure WebView Configurations
- 🔓 Sensitive Information Disclosure
- 🛡️ Android Security Misconfigurations

---

# 🎯 Expected Outcomes

Upon successful completion of this lab, you will have:

- ✔️ Decompiled Android APK files
- ✔️ Analyzed AndroidManifest.xml
- ✔️ Reviewed Java source code
- ✔️ Identified hardcoded secrets
- ✔️ Automated APK analysis using Python
- ✔️ Generated JSON security reports
- ✔️ Created HTML assessment reports
- ✔️ Built reusable mobile security tools
- ✔️ Improved Android application assessment skills

---

# 👨‍💻 Target Audience

This lab is ideal for:

- Mobile Application Security Engineers
- Android Developers
- Penetration Testers
- Reverse Engineers
- Malware Analysts
- Product Security Engineers
- Security Researchers
- DevSecOps Engineers
- Security Consultants
- Bug Bounty Hunters
- SOC Analysts
- Cybersecurity Students

---

# 📖 Prerequisites

Before starting this lab, learners should have:

- 📱 Basic Android application knowledge
- 💻 Linux command-line experience
- ☕ Basic Java programming
- 🐍 Basic Python programming
- 🔐 Mobile application security fundamentals
- 🛡️ General cybersecurity knowledge

---

# 🌟 Why This Lab Matters

Android applications often contain sensitive information, insecure configurations, and implementation flaws that can expose users and organizations to security risks. Security professionals routinely perform static analysis to discover vulnerabilities before applications are deployed or released.

This lab teaches the complete Android security assessment workflow using industry-standard reverse engineering tools. By combining APK decompilation, source code review, secret detection, and automated reporting, learners gain practical skills required for mobile penetration testing, vulnerability research, malware analysis, secure application development, and product security assessments.

---

# 💼 Real-World Applications

The techniques covered in this lab are commonly used for:

- 📱 Mobile Application Penetration Testing
- 🛡️ Secure Code Reviews
- 🔍 Android Malware Analysis
- 🔐 Product Security Assessments
- 📊 Security Compliance Audits
- 🚀 Secure Software Development Lifecycle (SSDLC)
- ☁️ DevSecOps Mobile Security
- 🧪 Vulnerability Research
- 🏢 Enterprise Mobile Security Reviews

---

# ⚠️ Disclaimer

This lab is intended solely for educational purposes and authorized mobile application security testing. Only analyze Android applications that you own or have explicit permission to assess. Unauthorized reverse engineering or security testing may violate software licenses, organizational policies, or applicable laws.

---

# ⭐ Key Takeaway

By completing this lab, you will gain practical experience using industry-standard Android reverse engineering and security analysis tools to decompile APK files, inspect source code, discover sensitive information, automate vulnerability assessments, and generate professional security reports—essential skills for modern mobile application security professionals.
