#!/usr/bin/env python3
"""
CVSS v3.1 Calculator
Students: Complete the TODO sections to implement CVSS scoring
"""

import json
import math
from typing import Dict, List

class CVSSCalculator:
    """CVSS v3.1 Base Score Calculator"""
    
    # CVSS v3.1 metric values
    ATTACK_VECTOR = {
        'Network': 0.85,
        'Adjacent': 0.62,
        'Local': 0.55,
        'Physical': 0.2
    }
    
    ATTACK_COMPLEXITY = {
        'Low': 0.77,
        'High': 0.44
    }
    
    PRIVILEGES_REQUIRED = {
        'None': 0.85,
        'Low': 0.62,
        'High': 0.27
    }
    
    PRIVILEGES_REQUIRED_CHANGED = {
        'None': 0.85,
        'Low': 0.68,
        'High': 0.5
    }
    
    USER_INTERACTION = {
        'None': 0.85,
        'Required': 0.62
    }
    
    IMPACT_METRICS = {
        'None': 0.0,
        'Low': 0.22,
        'High': 0.56
    }
    
    def calculate_exploitability_score(self, av: float, ac: float, pr: float, ui: float) -> float:
        """
        Calculate exploitability score.
        Formula: 8.22 × AV × AC × PR × UI
        
        Args:
            av: Attack Vector value
            ac: Attack Complexity value
            pr: Privileges Required value
            ui: User Interaction value
        
        Returns:
            Exploitability score
        """
        # TODO: Implement exploitability calculation
        pass
    
    def calculate_impact_score(self, c: float, i: float, a: float, scope: str) -> float:
        """
        Calculate impact score based on CIA triad and scope.
        
        Args:
            c: Confidentiality impact value
            i: Integrity impact value
            a: Availability impact value
            scope: Scope (Unchanged or Changed)
        
        Returns:
            Impact score
        """
        # TODO: Calculate ISS = 1 - [(1-C) × (1-I) × (1-A)]
        # TODO: If scope is Unchanged: return 6.42 × ISS
        # TODO: If scope is Changed: return 7.52 × (ISS - 0.029) - 3.25 × (ISS - 0.02)^15
        pass
    
    def calculate_base_score(self, exploitability: float, impact: float, scope: str) -> float:
        """
        Calculate CVSS base score.
        
        Args:
            exploitability: Exploitability score
            impact: Impact score
            scope: Scope value
        
        Returns:
            CVSS base score (0.0-10.0)
        """
        # TODO: If impact <= 0, return 0.0
        # TODO: If scope is Unchanged: score = min(impact + exploitability, 10)
        # TODO: If scope is Changed: score = min(1.08 × (impact + exploitability), 10)
        # TODO: Return math.ceil(score * 10) / 10
        pass
    
    def get_severity_rating(self, score: float) -> str:
        """
        Get severity rating based on CVSS score.
        
        Args:
            score: CVSS base score
        
        Returns:
            Severity rating string
        """
        # TODO: Implement severity rating logic
        # None: 0.0, Low: 0.1-3.9, Medium: 4.0-6.9, High: 7.0-8.9, Critical: 9.0-10.0
        pass
    
    def create_vector_string(self, vulnerability: Dict) -> str:
        """
        Create CVSS vector string.
        Format: CVSS:3.1/AV:X/AC:X/PR:X/UI:X/S:X/C:X/I:X/A:X
        
        Args:
            vulnerability: Vulnerability dictionary
        
        Returns:
            CVSS vector string
        """
        # TODO: Map full metric names to abbreviations
        # TODO: Construct vector string in proper format
        pass
    
    def calculate_cvss(self, vulnerability: Dict) -> Dict:
        """
        Calculate complete CVSS score for a vulnerability.
        
        Args:
            vulnerability: Vulnerability data dictionary
        
        Returns:
            Dictionary with CVSS scores and metrics
        """
        # TODO: Extract metric values from vulnerability dict
        # TODO: Handle PR value based on scope (use PRIVILEGES_REQUIRED_CHANGED if scope is Changed)
        # TODO: Calculate exploitability, impact, and base scores
        # TODO: Get severity rating
        # TODO: Create vector string
        # TODO: Return complete result dictionary
        pass
    
    def process_vulnerabilities_file(self, filename: str) -> List[Dict]:
        """
        Process vulnerabilities from JSON file.
        
        Args:
            filename: Path to JSON file
        
        Returns:
            List of vulnerability results with CVSS scores
        """
        # TODO: Load JSON file
        # TODO: Process each vulnerability
        # TODO: Return list of results
        pass

def main():
    """Main function to test CVSS calculator"""
    calculator = CVSSCalculator()
    
    print("CVSS v3.1 Calculator")
    print("=" * 50)
    
    # TODO: Process sample vulnerabilities file
    # TODO: Display results sorted by score
    # TODO: Print summary statistics

if __name__ == "__main__":
    main()
