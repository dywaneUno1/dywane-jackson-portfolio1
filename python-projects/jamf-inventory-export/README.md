# Jamf Pro Inventory Export Tool

A Python script to export device inventory data from Jamf Pro MDM system to CSV format for reporting and analysis.

## Features

- 🔐 Secure authentication using bearer tokens
- 📊 Export computer inventory to CSV
- 🛡️ Environment variable support for credentials
- ✅ Error handling and status reporting

## Prerequisites

- Python 3.7+
- Jamf Pro API access credentials
- Active Jamf Pro instance

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Set environment variables for secure credential management:

```bash
export JAMF_URL="https://your-instance.jamfcloud.com"
export JAMF_USERNAME="your-api-username"
export JAMF_PASSWORD="your-api-password"
```

## Usage

Run the script:
```bash
python inventory_export.py
```

## Author

Gwane Jackson  
Employed by Apple Inc - Previous Client Engineering IS&T:
Jamf 300 Certified Admin 
