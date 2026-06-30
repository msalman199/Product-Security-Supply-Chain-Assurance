#!/usr/bin/env python3
# File: config.py

# Capture Configuration
CAPTURE_INTERFACE = 'any'
CAPTURE_DURATION = 300  # seconds
CAPTURE_FILTER = 'not port 22'

# Traffic Generation
HTTP_ENDPOINTS = [
    'http://httpbin.org/get',
    'http://httpbin.org/post'
]

DNS_DOMAINS = [
    'product-security.example.com',
    'api.security-scanner.com'
]

# Analysis Settings
ANOMALY_THRESHOLD = 3  # Standard deviations
COMMON_PORTS = {80, 443, 53, 22}

# Output Settings
OUTPUT_DIR = './analysis_output'
GENERATE_VISUALIZATIONS = True
