#!/bin/bash

# Master Service Enumeration Script
# Combines nmap, netstat, and Python automation

TARGET="localhost"
OUTPUT_DIR="master_enumeration_$(date +%Y%m%d_%H%M%S)"

echo "Starting Master Service Enumeration"
echo "Target: $TARGET"
echo "Output Directory: $OUTPUT_DIR"
echo "=================================="

# Create output directory
mkdir -p $OUTPUT_DIR

# Phase 1: Basic nmap scanning
echo "Phase 1: Basic nmap scanning..."
nmap $TARGET > $OUTPUT_DIR/nmap_basic.txt
nmap -sV $TARGET > $OUTPUT_DIR/nmap_services.txt
nmap -A $TARGET > $OUTPUT_DIR/nmap_aggressive.txt

# Phase 2: netstat analysis
echo "Phase 2: netstat analysis..."
netstat -ln > $OUTPUT_DIR/netstat_listening.txt
netstat -an > $OUTPUT_DIR/netstat_all.txt
netstat -lnp > $OUTPUT_DIR/netstat_processes.txt

# Phase 3: Python automation
echo "Phase 3: Python automation..."
cd $OUTPUT_DIR
python3 ../service_enumeration.py
python3 ../advanced_nmap_scripts.py
cd ..

# Phase 4: Generate summary
echo "Phase 4: Generating summary..."
{
    echo "Master Enumeration Summary"
    echo "========================="
    echo "Date: $(date)"
    echo "Target: $TARGET"
    echo ""
    echo "Open Ports (nmap):"
    grep "open" $OUTPUT_DIR/nmap_basic.txt
    echo ""
    echo "Listening Ports (netstat):"
    grep "LISTEN" $OUTPUT_DIR/netstat_listening.txt | awk '{print $4}' | sort -u
    echo ""
    echo "Active Connections:"
    grep "ESTABLISHED" $OUTPUT_DIR/netstat_all.txt | wc -l
} > $OUTPUT_DIR/master_summary.txt

echo "Master enumeration completed!"
echo "Results saved in: $OUTPUT_DIR"
echo "Check master_summary.txt for overview"
