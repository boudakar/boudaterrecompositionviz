# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 05:06:52 2024

@author: pc
"""

import socket

def scan_ports(ip, ports):
    print(f"[INFO] Scannage de {ip}...")
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((ip, port))
                if result == 0:
                    print(f"[OUVERT] Port {port}")
                else:
                    print(f"[FERMÉ] Port {port}")
        except Exception as e:
            print(f"Erreur sur le port {port}: {e}")

# Exemple : scanner les ports 20 à 30 sur une machine distante
scan_ports("192.168.1.1", range(20, 31))
