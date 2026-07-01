<div align="center">

# 🔍 Decompile Binaries Using Ghidra & dotPeek

### Reverse Engineering & Static Vulnerability Analysis 

![Ghidra](https://img.shields.io/badge/Ghidra-10.4-4B0082?style=for-the-badge&logo=ghidra&logoColor=white)
![dotPeek](https://img.shields.io/badge/dotPeek-2023.2.3-000000?style=for-the-badge&logo=jetbrains&logoColor=white)
![Java](https://img.shields.io/badge/Java-17_JDK-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C](https://img.shields.io/badge/C-GCC-A8B9CC?style=for-the-badge&logo=c&logoColor=black)
![C%23](https://img.shields.io/badge/C%23-.NET-239120?style=for-the-badge&logo=csharp&logoColor=white)
![Wine](https://img.shields.io/badge/Wine-Compatibility_Layer-722F37?style=for-the-badge&logo=winerar&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Cloud_Lab-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Reverse_Engineering-CC0000?style=for-the-badge)

</div>

---

> ⚠️ **AUTHORIZED USE ONLY**
> This lab, including all binaries, code samples, and tooling, is provided strictly for **educational purposes** within the Al Nafi training environment. Reverse engineering, decompiling, or analyzing software you do not own or have explicit written authorization to test is **illegal** in most jurisdictions. Do not apply these techniques against production systems, third-party applications, or any binary you are not authorized to analyze.

---

## 📑 Table of Contents

- [🧰 Technology Stack](#-technology-stack)
- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment](#️-lab-environment)
- [📁 Directory Structure](#-directory-structure)
- [🔄 Analysis Workflow](#-analysis-workflow)
- [🧪 Task 1: Install Ghidra and Create Sample Binaries](#-task-1-install-ghidra-and-create-sample-binaries)
- [🧠 Task 2: Analyze Native Binaries with Ghidra](#-task-2-analyze-native-binaries-with-ghidra)
- [🪟 Task 3: Analyze .NET Assemblies with dotPeek](#-task-3-analyze-net-assemblies-with-dotpeek)
- [🤖 Task 4: Automate Analysis with Python](#-task-4-automate-analysis-with-python)
- [🛡️ Vulnerability & MITRE ATT&CK Reference](#️-vulnerability--mitre-attck-reference)
- [🧯 Troubleshooting](#-troubleshooting)
- [✅ Expected Outcomes](#-expected-outcomes)
- [📌 Key Takeaways](#-key-takeaways)
- [🚀 Next Steps](#-next-steps)

---

## 🧰 Technology Stack

| Technology | Purpose | Badge |
|---|---|---|
| **Ghidra** | NSA open-source SRE suite for decompiling native binaries | ![Ghidra](https://img.shields.io/badge/Ghidra-Reverse_Engineering-4B0082?style=flat-square&logo=ghidra&logoColor=white) |
| **dotPeek** | JetBrains .NET decompiler for C# assembly analysis | ![dotPeek](https://img.shields.io/badge/dotPeek-.NET_Decompiler-000000?style=flat-square&logo=jetbrains&logoColor=white) |
| **Wine** | Windows compatibility layer for running dotPeek on Linux | ![Wine](https://img.shields.io/badge/Wine-Compat_Layer-722F37?style=flat-square) |
| **GCC / Mono** | Compilers for building vulnerable C and C# test binaries | ![GCC](https://img.shields.io/badge/GCC-Compiler-A8B9CC?style=flat-square) ![Mono](https://img.shields.io/badge/Mono-.NET_Runtime-512BD4?style=flat-square) |
| **Python 3** | Automation scripting for headless Ghidra analysis | ![Python](https://img.shields.io/badge/Python-Automation-3776AB?style=flat-square&logo=python&logoColor=white) |
| **Java 17 (OpenJDK)** | Runtime dependency required by Ghidra | ![Java](https://img.shields.io/badge/Java-OpenJDK_17-ED8B00?style=flat-square&logo=openjdk&logoColor=white) |

---

## 🎯 Objectives

| # | Objective |
|---|---|
| 1 | Install and configure Ghidra for binary reverse engineering |
| 2 | Decompile native Linux binaries and identify security vulnerabilities |
| 3 | Use dotPeek to analyze .NET assemblies |
| 4 | Automate binary analysis using Ghidra's headless mode |
| 5 | Generate security assessment reports from decompiled code |

---

## 📋 Prerequisites

| # | Requirement |
|---|---|
| 1 | Basic understanding of C/C++ and C# programming |
| 2 | Familiarity with Linux command line |
| 3 | Knowledge of common security vulnerabilities (buffer overflows, SQL injection) |
| 4 | Understanding of binary file formats (ELF, PE) |

---

## 🖥️ Lab Environment

> 💡 Al Nafi provides ready-to-use Linux-based cloud machines for this lab. Click **Start Lab** to access your pre-configured environment with all necessary tools installed.

---

## 📁 Directory Structure

```
lab11-binary-analysis/
├── ghidra/                          # Ghidra 10.4 installation
│   ├── ghidraRun
│   └── support/analyzeHeadless
├── ghidra_projects/
│   └── BinaryAnalysis/              # Ghidra project workspace
├── vulnerable_app.c                 # Vulnerable native C source
├── vulnerable_app                   # Compiled ELF binary
├── VulnerableApp.cs                 # Vulnerable .NET source
├── VulnerableApp.exe                # Compiled .NET assembly
├── dotpeek_output/                  # Exported dotPeek decompilation
├── analysis_report.md               # Native binary findings
├── dotnet_analysis.md               # .NET assembly findings
├── automated_analysis.py            # Python automation script
├── FindVulnerabilities.java         # Ghidra headless script
└── automated_analysis/
    └── analysis_report.json         # Automated scan output
```

---

## 🔄 Analysis Workflow

```
                         ┌────────────────────────┐
                         │   Vulnerable Sources    │
                         │  (C  +  C#)             │
                         └───────────┬────────────┘
                                     │  compile
                    ┌────────────────┴────────────────┐
                    ▼                                  ▼
          ┌───────────────────┐              ┌───────────────────┐
          │  vulnerable_app    │              │ VulnerableApp.exe │
          │  (ELF Binary)      │              │ (.NET Assembly)   │
          └─────────┬──────────┘              └─────────┬─────────┘
                    │                                    │
                    ▼                                    ▼
          ┌───────────────────┐              ┌───────────────────┐
          │      Ghidra        │              │      dotPeek       │
          │  (Headless/GUI)    │              │  (via Wine)         │
          └─────────┬──────────┘              └─────────┬─────────┘
                    │  decompile                         │  decompile
                    ▼                                    ▼
          ┌───────────────────┐              ┌───────────────────┐
          │ Decompiled C Code  │              │ Decompiled C# Code │
          └─────────┬──────────┘              └─────────┬─────────┘
                    │                                    │
                    └────────────────┬───────────────────┘
                                     ▼
                       ┌─────────────────────────┐
                       │  Vulnerability Report     │
                       │  (Markdown / JSON)        │
                       └─────────────────────────┘
```

---

## 🧪 Task 1: Install Ghidra and Create Sample Binaries

### 🔧 Step 1.1: Install Ghidra

```bash
# Update system and install Java
sudo apt update && sudo apt install openjdk-17-jdk -y

# Create working directory
mkdir -p ~/lab11-binary-analysis
cd ~/lab11-binary-analysis

# Download and extract Ghidra
wget https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.4_build/ghidra_10.4_PUBLIC_20230928.zip
unzip ghidra_10.4_PUBLIC_20230928.zip
mv ghidra_10.4_PUBLIC ghidra
chmod +x ghidra/ghidraRun

# Verify installation
./ghidra/ghidraRun --version
```

✅ **Checkpoint:** Ghidra should launch without errors and report its version.

### 🐛 Step 1.2: Create Vulnerable Test Binary

Create a C program with intentional vulnerabilities:

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void buffer_overflow_vuln(char* input) {
    char buffer[64];
    strcpy(buffer, input);  // Vulnerability: no bounds checking
    printf("Data: %s\n", buffer);
}

void format_string_vuln(char* input) {
    printf(input);  // Vulnerability: format string
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }

    // Vulnerability: command injection
    char cmd[256];
    snprintf(cmd, sizeof(cmd), "echo %s", argv[1]);
    system(cmd);

    buffer_overflow_vuln(argv[1]);
    return 0;
}
```

```bash
# Compile with security features disabled for analysis
gcc -o vulnerable_app vulnerable_app.c -fno-stack-protector -z execstack -no-pie
```

⚠️ **Note:** Security mitigations are intentionally disabled (`-fno-stack-protector`, `-z execstack`, `-no-pie`) so the vulnerabilities remain visible for teaching purposes — never ship production code this way.

### 🍷 Step 1.3: Install Wine and dotPeek

```bash
# Install Wine for Windows applications
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install wine64 wine32 -y

# Configure Wine
winecfg  # Set to Windows 10, then close

# Download dotPeek
mkdir -p ~/.wine/drive_c/dotpeek
cd ~/.wine/drive_c/dotpeek
wget https://download.jetbrains.com/resharper/dotUltimate.2023.2.3/JetBrains.dotPeek.2023.2.3.exe
wine JetBrains.dotPeek.2023.2.3.exe  # Follow installation wizard
```

### 🧷 Step 1.4: Create Vulnerable .NET Assembly

```csharp
using System;
using System.Data.SqlClient;
using System.IO;

namespace VulnerableApp
{
    class Program
    {
        // Hardcoded credentials
        private static string API_KEY = "sk-1234567890abcdef";

        // SQL Injection vulnerability
        public static void LoginUser(string username, string password)
        {
            string query = "SELECT * FROM Users WHERE Username='" +
                          username + "' AND Password='" + password + "'";
            // Execute query (vulnerability present)
        }

        // Path traversal vulnerability
        public static string ReadFile(string filename)
        {
            string path = "/var/data/" + filename;  // No validation
            return File.ReadAllText(path);
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Vulnerable .NET Application");
        }
    }
}
```

```bash
# Install Mono and compile
sudo apt install mono-devel -y
mcs VulnerableApp.cs -out:VulnerableApp.exe
```

---

## 🧠 Task 2: Analyze Native Binaries with Ghidra

### 📂 Step 2.1: Create Ghidra Project

```bash
# Launch Ghidra
cd ~/lab11-binary-analysis
./ghidra/ghidraRun &
```

**In Ghidra GUI:**
1. `File → New Project → Non-Shared Project`
2. Set directory: `~/lab11-binary-analysis/ghidra_projects`
3. Name: `BinaryAnalysis`
4. Click **Finish**

### 📥 Step 2.2: Import and Analyze Binary

1. Click **Import File** (dragon icon)
2. Select `vulnerable_app` binary
3. Accept default settings → **OK**
4. Double-click imported file to open **CodeBrowser**
5. When prompted, click **Yes** to analyze
6. In Analysis Options:
   - ☑️ Check **"Decompiler Parameter ID"**
   - ☑️ Check **"Function Start Search"**
7. Click **Analyze**

### 🔎 Step 2.3: Examine Decompiled Code

Navigate the analysis:

1. **Symbol Tree** (left panel) → **Functions** → `main`
2. View decompiled C code in **Decompiler** window (right)
3. Locate `buffer_overflow_vuln` function
4. Identify the `strcpy` call without bounds checking
5. Find `format_string_vuln` with unsafe `printf`
6. Note `system()` call with user input

### 📝 Step 2.4: Document Vulnerabilities

Create analysis report template:

```bash
cat > analysis_report.md << 'EOF'
# Binary Analysis Report

## Binary: vulnerable_app

### Vulnerability 1: Buffer Overflow
- **Function**: buffer_overflow_vuln()
- **Location**: strcpy() call
- **Risk**: High
- **Description**: TODO - Describe the vulnerability
- **Recommendation**: TODO - Suggest fix

### Vulnerability 2: Format String
- **Function**: format_string_vuln()
- **Location**: printf() call
- **Risk**: Medium
- **Description**: TODO - Describe the vulnerability
- **Recommendation**: TODO - Suggest fix

### Vulnerability 3: Command Injection
- **Function**: main()
- **Location**: system() call
- **Risk**: High
- **Description**: TODO - Describe the vulnerability
- **Recommendation**: TODO - Suggest fix
EOF
```

🎓 **Student Task:** Complete the `TODO` sections by analyzing the decompiled code.

---

## 🪟 Task 3: Analyze .NET Assemblies with dotPeek

### 🚀 Step 3.1: Launch dotPeek

```bash
# Start dotPeek
cd ~/.wine/drive_c/Program\ Files/JetBrains/JetBrains\ dotPeek\ 2023.2.3/bin
wine dotPeek64.exe &
```

### 📦 Step 3.2: Decompile Assembly

**In dotPeek:**
1. `File → Open`
2. Navigate to `VulnerableApp.exe`
3. Expand assembly tree: `VulnerableApp → Program`
4. Examine each method

### 🕵️ Step 3.3: Identify .NET Vulnerabilities

Analyze the decompiled code for:

| Vulnerability | Location |
|---|---|
| 💉 SQL Injection | String concatenation in `LoginUser()` |
| 📁 Path Traversal | Unvalidated path in `ReadFile()` |
| 🔑 Hardcoded Secrets | `API_KEY` field in plain text |

### 📤 Step 3.4: Export and Document

**Export decompiled source:**
1. Right-click assembly → **Export to Project**
2. Output: `~/lab11-binary-analysis/dotpeek_output`
3. Click **Export**

Create .NET analysis report template:

```bash
cat > dotnet_analysis.md << 'EOF'
# .NET Assembly Analysis Report

## Assembly: VulnerableApp.exe

### Vulnerability 1: SQL Injection
- **Method**: LoginUser()
- **Risk**: Critical
- **Details**: TODO - Analyze the SQL query construction
- **Fix**: TODO - Recommend parameterized queries

### Vulnerability 2: Path Traversal
- **Method**: ReadFile()
- **Risk**: High
- **Details**: TODO - Analyze path handling
- **Fix**: TODO - Recommend validation approach

### Vulnerability 3: Hardcoded Credentials
- **Field**: API_KEY
- **Risk**: High
- **Details**: TODO - Document the exposure
- **Fix**: TODO - Recommend secure storage
EOF
```

🎓 **Student Task:** Complete the analysis by examining the decompiled C# code.

---

## 🤖 Task 4: Automate Analysis with Python

### 🛠️ Step 4.1: Create Automation Script Template

```python
#!/usr/bin/env python3
"""
Automated binary analysis using Ghidra headless mode
"""

import subprocess
import os
import json
from pathlib import Path

class GhidraAnalyzer:
    def __init__(self, ghidra_path, project_path):
        """
        Initialize Ghidra analyzer

        Args:
            ghidra_path: Path to Ghidra installation
            project_path: Path for analysis projects
        """
        self.ghidra_path = Path(ghidra_path)
        self.project_path = Path(project_path)
        self.headless_script = self.ghidra_path / "support" / "analyzeHeadless"

    def analyze_binary(self, binary_path, project_name="AutoAnalysis"):
        """
        Analyze binary using Ghidra headless mode

        Args:
            binary_path: Path to binary file
            project_name: Name for Ghidra project

        Returns:
            Dictionary with analysis results
        """
        # TODO: Validate binary_path exists
        # TODO: Construct headless analysis command
        # TODO: Execute analysis with subprocess
        # TODO: Parse and return results
        pass

    def batch_analyze(self, binary_directory):
        """
        Analyze multiple binaries in directory

        Args:
            binary_directory: Directory containing binaries

        Returns:
            List of analysis results
        """
        # TODO: Find executable files in directory
        # TODO: Analyze each binary
        # TODO: Collect and return results
        pass

def generate_report(results, output_file):
    """
    Generate JSON report from analysis results

    Args:
        results: Analysis results dictionary
        output_file: Path for output report
    """
    # TODO: Format results as JSON
    # TODO: Calculate summary statistics
    # TODO: Write to output file
    pass

def main():
    # Configuration
    config = {
        "ghidra_path": "~/lab11-binary-analysis/ghidra",
        "project_path": "~/lab11-binary-analysis/automated_analysis",
        "binary_directory": "~/lab11-binary-analysis"
    }

    # TODO: Expand paths
    # TODO: Create analyzer instance
    # TODO: Run batch analysis
    # TODO: Generate report
    pass

if __name__ == "__main__":
    main()
```

🎓 **Student Task:** Implement the `TODO` sections to create a working automation tool.

### ⚙️ Step 4.2: Create Ghidra Post-Analysis Script Template

```java
// FindVulnerabilities.java
// Ghidra script to detect common vulnerabilities
// @category Analysis

import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.*;
import ghidra.program.model.symbol.*;

public class FindVulnerabilities extends GhidraScript {

    @Override
    public void run() throws Exception {
        println("=== Vulnerability Analysis ===");

        // TODO: Implement findDangerousFunctions()
        // TODO: Implement findFormatStringVulns()
        // TODO: Implement findBufferOperations()

        println("=== Analysis Complete ===");
    }

    private void findDangerousFunctions() {
        // TODO: Search for strcpy, strcat, sprintf, gets, system
        // TODO: Find references to these functions
        // TODO: Report locations
    }

    private void findFormatStringVulns() {
        // TODO: Search for printf-family functions
        // TODO: Analyze call sites
        // TODO: Report potential vulnerabilities
    }

    private void findBufferOperations() {
        // TODO: Iterate through functions
        // TODO: Find stack allocations
        // TODO: Report buffer operations
    }
}
```

🎓 **Student Task:** Complete the vulnerability detection logic.

### ▶️ Step 4.3: Run Automated Analysis

```bash
# Make script executable
chmod +x automated_analysis.py

# Run analysis
python3 automated_analysis.py

# View results
cat ~/lab11-binary-analysis/automated_analysis/analysis_report.json
```

---

## 🛡️ Vulnerability & MITRE ATT&CK Reference

| Vulnerability | CWE ID | Related ATT&CK Technique | Tactic |
|---|---|---|---|
| Stack Buffer Overflow | CWE-121 | [T1203 – Exploitation for Client Execution](https://attack.mitre.org/techniques/T1203/) | Execution |
| Format String Vulnerability | CWE-134 | [T1190 – Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) | Initial Access |
| OS Command Injection | CWE-78 | [T1059 – Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/) | Execution |
| SQL Injection | CWE-89 | [T1190 – Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) | Initial Access |
| Path Traversal | CWE-22 | [T1083 – File and Directory Discovery](https://attack.mitre.org/techniques/T1083/) | Discovery |
| Hardcoded Credentials | CWE-798 | [T1552.001 – Unsecured Credentials: Credentials In Files](https://attack.mitre.org/techniques/T1552/001/) | Credential Access |

---

## 🧯 Troubleshooting

<details>
<summary>🔴 Ghidra Won't Start</summary>

- Verify Java 17 is installed: `java -version`
- Check Ghidra permissions: `chmod +x ghidra/ghidraRun`
- Review logs: `~/lab11-binary-analysis/ghidra/ghidra.log`

</details>

<details>
<summary>🟠 dotPeek Installation Issues</summary>

- Ensure Wine is properly configured: `winecfg`
- Try the 32-bit version if 64-bit fails
- Check Wine logs: `~/.wine/drive_c/users/*/Temp/`

</details>

<details>
<summary>🟡 Headless Analysis Fails</summary>

- Verify binary is executable: `file vulnerable_app`
- Check project path permissions
- Increase timeout in `subprocess.run()`

</details>

---

## ✅ Expected Outcomes

| Deliverable | Description |
|---|---|
| 🧠 Ghidra Analysis | Identified 3+ vulnerabilities in native binary |
| 🪟 dotPeek Analysis | Documented .NET security issues |
| 🤖 Automation Script | Working Python tool for batch analysis |
| 📄 Reports | Comprehensive security assessment documents |

---

## 📌 Key Takeaways

| Skill | Outcome |
|---|---|
| Decompilation | Decompile native and .NET binaries |
| Static Analysis | Identify security vulnerabilities through static analysis |
| Automation | Automate analysis workflows with Python |
| Reporting | Generate professional security reports |

These skills are essential for security auditing, malware analysis, and vulnerability research.

---

## 🚀 Next Steps

- Apply these techniques to analyze real-world applications (with proper authorization)
- Explore Ghidra's advanced features (scripting API, debugging)
- Study malware samples in controlled, isolated environments

---

<div align="center">

**Built with ❤️ for the next generation of cybersecurity professionals.**

</div>
