#!/bin/bash
# Comprehensive Firmware Analysis Script

FIRMWARE_FILE="$1"
ANALYSIS_DIR="comprehensive_analysis_$(basename "$FIRMWARE_FILE" .bin)"

if [ -z "$FIRMWARE_FILE" ]; then
    echo "Usage: $0 <firmware_file>"
    exit 1
fi

if [ ! -f "$FIRMWARE_FILE" ]; then
    echo "Error: Firmware file '$FIRMWARE_FILE' not found"
    exit 1
fi

echo "=========================================="
echo "COMPREHENSIVE FIRMWARE ANALYSIS"
echo "=========================================="
echo "Firmware: $FIRMWARE_FILE"
echo "Analysis Directory: $ANALYSIS_DIR"
echo "=========================================="

# Create analysis directory
mkdir -p "$ANALYSIS_DIR"
cd "$ANALYSIS_DIR"

# Step 1: Basic binwalk analysis
echo "[1/6] Running basic binwalk analysis..."
binwalk "../$FIRMWARE_FILE" > binwalk_analysis.txt
echo "    Results saved to: binwalk_analysis.txt"

# Step 2: Entropy analysis
echo "[2/6] Running entropy analysis..."
binwalk -E "../$FIRMWARE_FILE" > entropy_analysis.txt
echo "    Results saved to: entropy_analysis.txt"

# Step 3: Extract firmware
echo "[3/6] Extracting firmware..."
binwalk -e "../$FIRMWARE_FILE"
EXTRACTED_DIR="_$(basename "$FIRMWARE_FILE").extracted"

# Step 4: File system analysis
echo "[4/6] Analyzing filesystem..."
if [ -d "$EXTRACTED_DIR" ]; then
    find "$EXTRACTED_DIR" -type f | wc -l > filesystem_stats.txt
    echo "Total files: $(cat filesystem_stats.txt)" >> filesystem_stats.txt
    find "$EXTRACTED_DIR" -name "*.conf" -o -name "*.cfg" | wc -l >> filesystem_stats.txt
    echo "Configuration files found: $(tail -1 filesystem_stats.txt)" 
fi

# Step 5: Security analysis
echo "[5/6] Running security analysis..."
if [ -d "$EXTRACTED_DIR" ]; then
    # Search for credentials
    grep -r -i "password\|passwd\|secret" "$EXTRACTED_DIR" 2>/dev/null | head -10 > security_findings.txt
    
    # Search for private keys
    find "$EXTRACTED_DIR" -name "*.key" -o -name "*.pem" >> security_findings.txt
    
    # Search for executables
    find "$EXTRACTED_DIR" -type f -executable | head -20 >> security_findings.txt
fi

# Step 6: Generate summary report
echo "[6/6] Generating summary report..."
cat > analysis_summary.txt << EOF
FIRMWARE ANALYSIS SUMMARY
========================
Firmware File: $FIRMWARE_FILE
Analysis Date: $(date)
Analysis Directory: $ANALYSIS_DIR

BINWALK ANALYSIS:
$(head -20 binwalk_analysis.txt)

FILESYSTEM STATISTICS:
$(cat filesystem_stats.txt 2>/dev/null || echo "No filesystem statistics available")

SECURITY FINDINGS:
$(head -10 security_findings.txt 2>/dev/null || echo "No security findings available")

FILES GENERATED:
- binwalk_analysis.txt: Basic binwalk output
- entropy_analysis.txt: Entropy analysis results
- filesystem_stats.txt: Filesystem statistics
- security_findings.txt: Security analysis results
- $EXTRACTED_DIR/: Extracted firmware components

RECOMMENDATIONS:
1. Review configuration files for hardcoded credentials
2. Analyze executable files for security vulnerabilities
3. Check file permissions for overly permissive settings
4. Validate cryptographic implementations
5. Test web interfaces for common vulnerabilities
EOF

echo "=========================================="
echo "ANALYSIS COMPLETE"
echo "=========================================="
echo "Summary report: $ANALYSIS_DIR/analysis_summary.txt"
echo "Extracted files: $ANALYSIS_DIR/$EXTRACTED_DIR/"
echo "=========================================="
