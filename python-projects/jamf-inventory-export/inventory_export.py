#!/usr/bin/env python3
"""
Jamf Pro Inventory Export Script
Exports device inventory data from Jamf Pro API to CSV format
"""

import requests
import csv
import json
from datetime import datetime
import os
from requests.auth import HTTPBasicAuth


class JamfInventoryExporter:
    """Export inventory data from Jamf Pro"""
    
    def __init__(self, jamf_url, username, password):
        """
        Initialize the Jamf exporter
        
        Args:
            jamf_url: Base URL of Jamf Pro instance (e.g., https://company.jamfcloud.com)
            username: Jamf Pro API username
            password: Jamf Pro API password
        """
        self.jamf_url = jamf_url.rstrip('/')
        self.username = username
        self.password = password
        self.token = None
        
    def authenticate(self):
        """Authenticate with Jamf Pro API and get bearer token"""
        auth_url = f"{self.jamf_url}/api/v1/auth/token"
        
        try:
            response = requests.post(
                auth_url,
                auth=HTTPBasicAuth(self.username, self.password),
                headers={'Accept': 'application/json'}
            )
            response.raise_for_status()
            self.token = response.json()['token']
            print("✓ Successfully authenticated with Jamf Pro")
            return True
        except requests.exceptions.RequestException as e:
            print(f"✗ Authentication failed: {e}")
            return False
    
    def get_computers(self):
        """Retrieve all computer inventory records"""
        if not self.token:
            print("✗ Not authenticated. Call authenticate() first.")
            return []
        
        computers_url = f"{self.jamf_url}/JSSResource/computers"
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Accept': 'application/json'
        }
        
        try:
            response = requests.get(computers_url, headers=headers)
            response.raise_for_status()
            computers = response.json()['computers']
            print(f"✓ Retrieved {len(computers)} computer records")
            return computers
        except requests.exceptions.RequestException as e:
            print(f"✗ Failed to retrieve computers: {e}")
            return []
    
    def export_to_csv(self, computers, filename=None):
        """
        Export computer inventory to CSV file
        
        Args:
            computers: List of computer dictionaries
            filename: Output filename (optional)
        """
        if not computers:
            print("✗ No computer data to export")
            return
        
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'jamf_inventory_{timestamp}.csv'
        
        fieldnames = ['id', 'name', 'serial_number', 'udid', 'mac_address']
        
        try:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for computer in computers:
                    # Extract relevant fields
                    row = {
                        'id': computer.get('id', ''),
                        'name': computer.get('name', ''),
                        'serial_number': computer.get('serial_number', ''),
                        'udid': computer.get('udid', ''),
                        'mac_address': computer.get('mac_address', '')
                    }
                    writer.writerow(row)
            
            print(f"✓ Successfully exported {len(computers)} records to {filename}")
        except IOError as e:
            print(f"✗ Failed to write CSV file: {e}")


def main():
    """Main execution function"""
    # Load credentials from environment variables (recommended for security)
    jamf_url = os.getenv('JAMF_URL', 'https://your-instance.jamfcloud.com')
    username = os.getenv('JAMF_USERNAME', 'your-username')
    password = os.getenv('JAMF_PASSWORD', 'your-password')
    
    print("Jamf Pro Inventory Export Tool")
    print("=" * 40)
    
    # Initialize exporter
    exporter = JamfInventoryExporter(jamf_url, username, password)
    
    # Authenticate
    if not exporter.authenticate():
        return
    
    # Get computer inventory
    computers = exporter.get_computers()
    
    # Export to CSV
    if computers:
        exporter.export_to_csv(computers)


if __name__ == "__main__":
    main()
