# Python Network Scanner

A lightweight TCP port scanner with banner grabbing, built as part of my penetration testing practice.

## Features
- TCP connect scan on specified ports
- Banner grabbing for open services
- Clean output with timestamps
- Scans common ports (FTP, SSH, Telnet, SMTP, DNS, HTTP, SMB, MySQL)

## Requirements
- Python 3.x
- No external libraries needed (uses built-in socket)

## Usage
`bash
python3 scanner.py
Sample Output
=============================================

[+] Port 21: OPEN | Banner: 220 (vsFTPd 2.3.4)
[+] Port 22: OPEN | Banner: SSH-2.0-OpenSSH_4.7p1
[+] Port 80: OPEN | Banner: No banner

[*] Scan complete. 3 open ports found.
Disclaimer
This tool is intended for authorized penetration testing and educational purposes only.
Do not use against systems you do not own or have explicit permission to test.
Author
Rithul Surendran P P
BCA - Ethical Hacking, Digital Forensics & Cyber Security
Yenepoya University
