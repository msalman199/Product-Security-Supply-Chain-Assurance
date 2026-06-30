#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def load_security_data(filepath):
    """
    Load security events from CSV file.
    
    Args:
        filepath: Path to CSV file
    
    Returns:
        DataFrame with security events
    """
    # TODO: Load CSV using pandas
    # TODO: Convert timestamp column to datetime
    # TODO: Return the dataframe
    pass

def create_event_pie_chart(df, output_path):
    """
    Create pie chart showing event type distribution.
    
    Args:
        df: Security events dataframe
        output_path: Where to save the chart
    """
    # TODO: Count event types using value_counts()
    # TODO: Create figure with size (10, 8)
    # TODO: Generate pie chart with labels and percentages
    # TODO: Add title "Security Event Distribution"
    # TODO: Save figure to output_path with dpi=300
    pass

def create_severity_bar_chart(df, output_path):
    """
    Create bar chart showing severity levels.
    
    Args:
        df: Security events dataframe
        output_path: Where to save the chart
    """
    # TODO: Count severity levels
    # TODO: Define color mapping (critical=red, high=orange, medium=yellow, low=green)
    # TODO: Create bar chart with appropriate colors
    # TODO: Add value labels on top of bars
    # TODO: Add title and axis labels
    # TODO: Save figure
    pass

def main():
    """Main execution function"""
    # TODO: Load data from '../data/security_events.csv'
    # TODO: Create event distribution pie chart
    # TODO: Create severity bar chart
    # TODO: Print success messages
    pass

if __name__ == "__main__":
    main()
