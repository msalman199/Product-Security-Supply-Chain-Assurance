import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_telemetry_data():
    """
    Generate sample product telemetry data for IoT devices.
    Creates 5000 records with device metrics and anomalies.
    """
    np.random.seed(42)
    random.seed(42)
    
    # TODO: Define product types list
    # TODO: Define locations list
    # TODO: Set date range (30 days)
    
    telemetry_records = []
    
    # TODO: Loop to generate 5000 records
    # TODO: For each record, create timestamp
    # TODO: Generate device_id, product_type, location
    # TODO: Generate metrics based on product type:
    #       - temperature_celsius (use np.random.normal)
    #       - cpu_usage_percent
    #       - memory_usage_percent
    #       - power_consumption_watts
    #       - network_latency_ms
    #       - error_count
    # TODO: Add 5% anomalies (spike values randomly)
    # TODO: Append record dictionary to list
    
    # TODO: Create DataFrame from records
    # TODO: Sort by timestamp
    # TODO: Save to 'data/product_telemetry.csv'
    
    print(f"Generated telemetry data saved to data/product_telemetry.csv")

if __name__ == "__main__":
    generate_telemetry_data()
