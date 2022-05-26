
# Port Scanner & Network Enumerator

This project was created to imitate the popular Nmap scanning tool. However, it is no replacement as Nmap has a multitude more features and is more efficient. This is simply an instrument for learning about the reconnaissance stage of a cyber-attack. The scanner is only capable of local-network connections.


## Features

- SYN half-connect Scan
- SYN ACK full connect Scan
- NULL Scan
- FIN Scan
- XMAS Scan
- Hostname Sweep
- Ping (ARP) Sweep

## Lessons Learned

I undertook this project, as my first, to further educate myself on the TCP handshake process alongside the reconnaissance and enumeration techniques of a cyber-attack. Through this I have gained new skills in the Scapy Python library, and am now able to manipulate and create specialised packets.


## Dependencies
- Scapy (Version 2.4.5)
    
## Run Locally

Clone the repository

```bash
  git clone https://github.com/0xsys/tcpPortScanner
```

Go to the repository directory, then the src directory

```bash
  cd tcpPortScanner/src
```

Run the Python3 script

```bash
  sudo ./portScanner.py [cS][ssS][nS][xS][pS][fS][hS] 192.168.1.1
```

