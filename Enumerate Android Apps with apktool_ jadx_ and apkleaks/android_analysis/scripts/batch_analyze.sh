#!/bin/bash
# batch_analyze.sh

APK_DIR="$1"
OUTPUT_DIR="$2"

if [ -z "$APK_DIR" ] || [ -z "$OUTPUT_DIR" ]; then
    echo "Usage: ./batch_analyze.sh <apk_directory> <output_directory>"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

for apk in "$APK_DIR"/*.apk; do
    apk_name=$(basename "$apk" .apk)
    echo "[+] Analyzing $apk_name..."
    
    python3 scripts/comprehensive_analyzer.py "$apk" -o "$OUTPUT_DIR/$apk_name"
    python3 scripts/generate_report.py "$OUTPUT_DIR/$apk_name/comprehensive_analysis.json" "$OUTPUT_DIR/$apk_name/report.html"
done

echo "[+] Batch analysis complete. Results in $OUTPUT_DIR"
