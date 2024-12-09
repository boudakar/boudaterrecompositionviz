# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 05:12:57 2024

@author: pc
"""

import socket
import threading

MAX_CONNECTIONS = 5  # Limite de connexions simultanées

def monitor_and_limit(port):
    active_connections = 0
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(MAX_CONNECTIONS)
    print(f"[INFO] Limite de {MAX_CONNECTIONS} connexions sur le port {port}")

    while True:
        client, addr = server.accept()
        if active_connections >= MAX_CONNECTIONS:
            print(f"[ALERTE] Trop de connexions sur le port {port}. Connexion rejetée : {addr}")
            client.close()
        else:
            active_connections += 1
            print(f"[INFO] Connexion acceptée : {addr}")
            threading.Thread(target=handle_client, args=(client,)).start()

def handle_client(client_socket):
    client_socket.recv(1024)  # Simule la gestion de client
    client_socket.close()

monitor_and_limit(8080)
