# from scapy.all import ARP, Ether, srp

# # Define the target subnet (change to match your local network)
# target_ip = "192.168.1.0/24"

# # Create ARP request packet
# arp = ARP(pdst=target_ip)                         # Who has these IPs?
# ether = Ether(dst="ff:ff:ff:ff:ff:ff")            # Broadcast MAC address
# packet = ether / arp                              # Full Ethernet+ARP packet

# # Send packet and get response
# result = srp(packet, timeout=2, verbose=0)[0]     # srp sends & receives packets at Layer 2

# # Print active hosts
# for sent, received in result:
#     print(f"{received.psrc} is up, MAC: {received.hwsrc}")



import scapy.all as scapy
import sys
import os

def scan(ip_range):
    broadcast_mac = "ff:ff:ff:ff:ff:ff"
    for i in range(1, 255):  # Scan IPs from .1 to .254
        ip = f"{ip_range}.{i}"
        arp_request = scapy.ARP(pdst=ip)
        ether_request = scapy.Ether(dst=broadcast_mac)
        packet = ether_request / arp_request

        answered = scapy.srp(packet, timeout=1, verbose=0)[0]
        for sent, received in answered:
            print(f"{received.psrc} is up, MAC: {received.hwsrc}", flush=True)

def main():
    if os.geteuid() != 0:
        sys.exit("Run as root: sudo python3 setup.py")
    scan("10.32.1")

if __name__ == "__main__":
    main()
