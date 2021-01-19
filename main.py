#!/usr/bin/python3

import socket
import time
from datetime import datetime

IPS = ["8.8.8.8", "8.8.4.4", "1.1.1.1", "1.0.0.1"]
PORT = 53
RTRY = 3
TIMEOUT = 2

def check(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)
    for _ in range(RTRY):
        try:
            print(f"Trying ip {ip}")
            s.connect((ip, PORT))
            s.shutdown(socket.SHUT_RDWR)
            return True
        except Exception:
            time.sleep(2)
            continue
    return False

# main loop
while True:
    failed = []
    for ip in IPS:
        answer = check(ip)
        if not answer:
            failed.append(ip)
    if failed:
        for fail in failed:
            with open("host-down.log", "a+") as f:
                print(f"FAILED >> {fail} : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
                f.write(f"{fail} : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
    # Sleeper
    time.sleep(5*60)
