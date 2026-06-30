#!/bin/bash

# Network monitoring script using netstat
OUTPUT_DIR="netstat_results"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Create output directory
mkdir -p $OUTPUT_DIR

echo "Starting network connection analysis..."
echo "Timestamp: $(date)"

# Listening ports analysis
echo "Analyzing listening ports..."
netstat -ln > $OUTPUT_DIR/listening_ports_$TIMESTAMP.txt

# Active connections analysis
echo "Analyzing active connections..."
netstat -an > $OUTPUT_DIR/active_connections_$TIMESTAMP.txt

# Process-specific analysis
echo "Analyzing processes and ports..."
netstat -lnp > $OUTPUT_DIR/process_ports_$TIMESTAMP.txt

# Network statistics
echo "Gathering network statistics..."
netstat -s > $OUTPUT_DIR/network_stats_$TIMESTAMP.txt

# Create summary report
echo "Creating summary report..."
{
    echo "Network Analysis Summary - $(date)"
    echo "========================================"
    echo ""
    echo "Listening TCP Ports:"
    netstat -lnt | grep LISTEN | awk '{print $4}' | sort -u
    echo ""
    echo "Listening UDP Ports:"
    netstat -lnu | awk 'NR>2 {print $4}' | sort -u
    echo ""
    echo "Active Connection Count:"
    netstat -an | grep ESTABLISHED | wc -l
    echo ""
    echo "Top 10 Most Active Ports:"
    netstat -an | grep ESTABLISHED | awk '{print $4}' | cut -d: -f2 | sort | uniq -c | sort -nr | head -10
} > $OUTPUT_DIR/summary_$TIMESTAMP.txt

echo "Analysis completed. Results saved in $OUTPUT_DIR/"
