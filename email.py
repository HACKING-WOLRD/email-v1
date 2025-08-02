import os
import time
import random
import sys

# Colors
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'
P = '\033[95m'

def banner():
    os.system('clear')
    print(f"""{G}
██████╗ ██╗   ██╗██╗██╗     ███████╗
██╔══██╗╚██╗ ██╔╝██║██║     ██╔════╝
██████╔╝ ╚████╔╝ ██║██║     █████╗  
██╔═══╝   ╚██╔╝  ██║██║     ██╔══╝  
██║        ██║   ██║███████╗███████╗
╚═╝        ╚═╝   ╚═╝╚══════╝╚══════╝
{P}HACKING WORLD™ - ROOT EMAIL HACK TOOL
{Y}-------------------------------------------
""")

def loading_animation(text, duration=5):
    spinner = ['|', '/', '-', '\\']
    sys.stdout.write(Y + text + " ")
    for i in range(duration*4):
        sys.stdout.write(spinner[i % len(spinner)])
        sys.stdout.flush()
        time.sleep(0.25)
        sys.stdout.write('\b')
    print(W + "✓")

def request_root():
    print(f"\n{R}[!] Root Access Required...")
    time.sleep(2)
    print(f"{C}[✓] Requesting Root Permission...")
    time.sleep(2)
    print(f"{R}[X] Root Permission Denied!")
    print(f"{Y}[!] This Tool Works Only on Rooted Devices.")
    input(f"\n{W}Press Enter to Exit...")
    exit()

def main():
    banner()
    email = input(f"{C}[+] Enter Target Email Address: {W}")
    request_root()

main()