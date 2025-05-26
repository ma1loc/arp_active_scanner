# ARP Active Scanner

A Python-based tool for scanning local networks to discover active hosts through ARP (Address Resolution Protocol) requests.

## Features

- **Fast Scan Mode**: Quick network scanning but more noticeable on the network
- **Stealth Mode**: One-by-one scanning with random time delays for reduced network visibility
- **Automatic Interface Detection**: Can detect and use active network interfaces
- **MAC Vendor Lookup**: Displays vendor information for discovered MAC addresses
- **Colorized Output**: Uses color-coded terminal messages for better readability

## Prerequisites

- Python 3.x
- Root/Administrator privileges (required for raw socket operations)
- Linux/Unix operating system (some features may not work on Windows)

## Installation

1. Clone the repository or download the source code
2. Install the required dependencies:

```bash
pip install scapy netifaces mac-vendor-lookup
```

## Project Structure

```
arp_active_scanner/
├── arp_scan
│   └── arg_scan.py		# Main ARP scanning functionality
├── main.py				# Entry point for the application
├── parsing_scan
│   ├── parsing.py		# Command-line argument parsing
│   ├── rgb_msg.py		# Colored output functions
│   └── scan_utils.py	# Utility functions for scanning
└── README.md

3 directories, 6 files
```

## Usage

### Basic Usage

Run the scanner with root privileges and it will automatically detect an active interface and begin scanning:

```bash
sudo python main.py
```

### Specify Network Interface

```bash
sudo python main.py -i eth0
```

### Fast Scan Mode

```bash
sudo python main.py -i eth0 -f
```

### Stealth Mode

```bash
sudo python main.py -i eth0 -s
```

## Command Line Arguments

| Argument | Long Form | Description |
|----------|-----------|-------------|
| `-i` | `--interface` | Specify the network interface to use for scanning |
| `-f` | `--fast_scan` | Use fast scanning mode (noisy but quick) |
| `-s` | `--stealth` | Use stealth scanning mode (slower but less detectable) |

## Output Format

The scanner displays results in the following format:

```
IP Address         MAC Address              Vendor
---------------------------------------------------------------------------
192.168.1.1        aa:bb:cc:dd:ee:ff        Cisco Systems, Inc
192.168.1.5        11:22:33:44:55:66        Apple, Inc.
```

## You can use the Command to enable IP forwarding:
```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```
## To Disable it after you're done (for safety)
```bash
echo 0 > /proc/sys/net/ipv4/ip_forward
```

## How It Works

1. The scanner sends ARP requests to the broadcast address or individual IP addresses
2. Devices on the network respond with their MAC addresses
3. The tool collects these responses and displays them with vendor information
4. In stealth mode, it introduces random delays between scans to avoid detection

## Security and Ethical Use

This tool is intended for network administrators and security professionals to audit their own networks. Please ensure you have proper authorization before scanning any network.

## Troubleshooting

### Common Issues

- **"You must be root!!!"**: The application requires root privileges to send raw packets
- **"Interface does not have an IPv4 address"**: The selected interface doesn't have a valid IPv4 configuration
- **"Down OR No such device exists"**: The specified interface is either not found or not active

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
