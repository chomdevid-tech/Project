# Mini-IDPS

A lightweight network intrusion detection system that detects port scanning, brute force, and DOS attacks.

# Installation

Install required dependencies:
pip install scapy

# Usage
Run with root privileges:
sudo python3 main.py

# Testing Attacks

Port Scan (Nmap):
nmap <target_ip>

Brute Force FTP (Hydra):
hydra -l <username> -P <path_password_file> ftp://<target_ip>

DOS (Hping3):
sudo hping3 --flood <target_ip>

# Output
- Alerts.log - All detected attacks with timestamps
- block_ip.txt - List of blocked IPs
- Desktop popups - Real-time alert notifications
