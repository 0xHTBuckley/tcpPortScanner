#!/bin/bash python3

import socket

host = str(input("Please enter the IP: "))

def portScanner(host):
    for port in range(0,50000):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            if not s.connect_ex((host, port)):
                print(f"Port {port} is open")
                s.close()     
        except KeyboardInterrupt:
            print("\nYou have pressed CTRL+C")
            quit("Exitting!")

portScanner(host)