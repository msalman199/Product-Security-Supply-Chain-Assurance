#!/bin/bash

# Comprehensive nmap scanning script
TARGET="localhost"
OUTPUT_DIR="scan_results"

# Create output directory
mkdir -p $OUTPUT_DIR

echo "Starting comprehensive nmap scan of $TARGET"
echo "Results will be saved in $OUTPUT_DIR directory"

# Basic port scan
echo "Performing basic port scan..."
nmap $TARGET > $OUTPUT_DIR/basic_scan.txt

# Service version detection
echo "Performing service version detection..."
nmap -sV $TARGET > $OUTPUT_DIR/service_scan.txt

# Aggressive scan
echo "Performing aggressive scan..."
nmap -A $TARGET > $OUTPUT_DIR/aggressive_scan.txt

# UDP scan for common ports
echo "Performing UDP scan..."
sudo nmap -sU --top-ports 100 $TARGET > $OUTPUT_DIR/udp_scan.txt

# Script scan
echo "Performing script scan..."
nmap -sC $TARGET > $OUTPUT_DIR/script_scan.txt

echo "Scan completed. Check $OUTPUT_DIR for results."
