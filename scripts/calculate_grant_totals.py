#!/usr/bin/env python3
"""Calculate total grant amounts from grant_support.yaml, categorized by role.

This script parses the grant_support.yaml file and calculates:
- Total grants where Marine Denolle is lead PI
- Total grants where she is co-PI or co-I
- Overall grant total
- Number of grants in each category
"""

import re
import yaml
from pathlib import Path
from typing import Dict, List, Tuple


def parse_amount(area_text: str) -> Tuple[float, str]:
    """Extract dollar amount and role from grant area text.
    
    Args:
        area_text: The grant description containing amount and role
        
    Returns:
        Tuple of (amount in dollars, role)
    """
    # Extract dollar amount - handle formats like $500,000 or $735,074
    amount_match = re.search(r'\$([0-9,]+)', area_text)
    if not amount_match:
        return 0.0, "unknown"
    
    amount_str = amount_match.group(1).replace(',', '')
    amount = float(amount_str)
    
    # Extract role - look for (PI), (co-PI), (co-I), etc.
    role = "unknown"
    if re.search(r'\(PI\)', area_text):
        # Check if it's actually a lead PI role (not co-PI)
        if not re.search(r'\(co-PI\)', area_text):
            role = "lead-PI"
        else:
            role = "co-PI"
    elif re.search(r'\(co-PI\)', area_text):
        role = "co-PI"
    elif re.search(r'\(co-I\)', area_text):
        role = "co-I"
    
    # Special case: "PI, lead-PI Carl Tape" means she's PI but Carl Tape is lead
    if "lead-PI Carl Tape" in area_text or "lead-PI " in area_text.replace("(PI, lead-PI", "("):
        role = "co-PI"
    
    return amount, role


def calculate_grant_totals(yaml_file: Path) -> Dict[str, any]:
    """Calculate grant totals from YAML file.
    
    Args:
        yaml_file: Path to grant_support.yaml
        
    Returns:
        Dictionary with grant statistics
    """
    with open(yaml_file, 'r') as f:
        grants = yaml.safe_load(f)
    
    lead_pi_total = 0.0
    lead_pi_grants = []
    
    collaborative_total = 0.0
    collaborative_grants = []
    
    unknown_grants = []
    
    for grant in grants:
        institution = grant.get('institution', '')
        area = grant.get('area', '')
        year = grant.get('date', grant.get('start_date', ''))
        
        # Skip the summary entry
        if institution == 'Total Grant Support':
            continue
        
        # Skip range amounts like "Multiple SCEC grants"
        if 'each' in area.lower() and '-' in area:
            unknown_grants.append({
                'institution': institution,
                'area': area,
                'year': year,
                'note': 'Range amount not included in total'
            })
            continue
        
        amount, role = parse_amount(area)
        
        if amount == 0:
            unknown_grants.append({
                'institution': institution,
                'area': area,
                'year': year,
                'note': 'No amount found'
            })
            continue
        
        grant_info = {
            'institution': institution,
            'amount': amount,
            'year': year,
            'area': area
        }
        
        if role == "lead-PI":
            lead_pi_total += amount
            lead_pi_grants.append(grant_info)
        elif role in ["co-PI", "co-I"]:
            collaborative_total += amount
            collaborative_grants.append(grant_info)
        else:
            unknown_grants.append({
                **grant_info,
                'note': f'Unknown role: {role}'
            })
    
    return {
        'lead_pi_total': lead_pi_total,
        'lead_pi_grants': lead_pi_grants,
        'lead_pi_count': len(lead_pi_grants),
        'collaborative_total': collaborative_total,
        'collaborative_grants': collaborative_grants,
        'collaborative_count': len(collaborative_grants),
        'unknown_grants': unknown_grants,
        'grand_total': lead_pi_total + collaborative_total
    }


def format_currency(amount: float) -> str:
    """Format amount as currency string."""
    return f"${amount:,.0f}"


def print_report(stats: Dict):
    """Print a formatted report of grant statistics."""
    print("\n" + "="*80)
    print("GRANT FUNDING ANALYSIS")
    print("="*80)
    
    print(f"\n{'LEAD PI GRANTS':-^80}")
    print(f"Total Amount: {format_currency(stats['lead_pi_total'])}")
    print(f"Number of Grants: {stats['lead_pi_count']}\n")
    
    for grant in sorted(stats['lead_pi_grants'], key=lambda x: x['year'], reverse=True):
        print(f"  {grant['year']}  {grant['institution']:<40} {format_currency(grant['amount']):>15}")
    
    print(f"\n{'CO-PI / CO-I GRANTS':-^80}")
    print("Note: Co-PI indicates either lead PI on a multi-institution grant or")
    print("      co-PI for a collaborative grant within institutions.")
    print(f"Total Amount: {format_currency(stats['collaborative_total'])}")
    print(f"Number of Grants: {stats['collaborative_count']}\n")
    
    for grant in sorted(stats['collaborative_grants'], key=lambda x: x['year'], reverse=True):
        print(f"  {grant['year']}  {grant['institution']:<40} {format_currency(grant['amount']):>15}")
    
    if stats['unknown_grants']:
        print(f"\n{'EXCLUDED/UNKNOWN':-^80}")
        for grant in stats['unknown_grants']:
            year = grant.get('year', 'N/A')
            print(f"  {year}  {grant['institution']:<40} {grant.get('note', '')}")
    
    print(f"\n{'SUMMARY':-^80}")
    print(f"Lead PI Total:        {format_currency(stats['lead_pi_total']):>20}")
    print(f"Co-PI/Co-I Total:     {format_currency(stats['collaborative_total']):>20}")
    print(f"{'─'*80}")
    print(f"Grand Total:          {format_currency(stats['grand_total']):>20}")
    print(f"\nTotal Number of Grants Analyzed: {stats['lead_pi_count'] + stats['collaborative_count']}")
    print("="*80 + "\n")


def main():
    """Main entry point."""
    # Find the grant_support.yaml file
    script_dir = Path(__file__).parent
    yaml_file = script_dir.parent / 'marine-cv-docs' / 'grant_support.yaml'
    
    if not yaml_file.exists():
        print(f"Error: Could not find {yaml_file}")
        return 1
    
    stats = calculate_grant_totals(yaml_file)
    print_report(stats)
    
    return 0


if __name__ == '__main__':
    exit(main())
