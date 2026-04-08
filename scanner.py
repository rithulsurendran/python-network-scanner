#!/usr/bin/env python3
import socket
import sys
from datetime import datetime

def scan_ports(target, ports):
    print(f"\n{'='*50}")
    print(f"ZecurX Network Scanner")
    print(f"Target: {target}")
    print(f"Scan started: {datetime.now()}")
    print(f"{'='*50}\n")
    
    open_ports = []
    
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                try:
                    banner = sock.recv(1024).decode().strip()
                except:
                    banner = "No banner"
                print(f"[+] Port {port}: OPEN | Banner: {banner}")
                open_ports.append(port)
            sock.close()
        except Exception as e:
            pass
    
    print(f"\n[*] Scan complete. {len(open_ports)} open ports found.")
    return open_ports

if __name__ == "__main__":
    target = "192.168.56.101"
    ports = [21, 22, 23, 25, 53, 80, 139, 445, 3306, 8180]
    scan_ports(target, ports)
