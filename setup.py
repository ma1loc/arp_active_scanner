#!/usr/bin/env python3

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║                                                                          ║
# ║             ███╗   ███╗ █████╗  ██╗██╗      ██████╗  ██████╗             ║
# ║             ████╗ ████║██╔══██╗███║██║     ██╔═══██╗██╔════╝             ║
# ║             ██╔████╔██║███████║╚██║██║     ██║   ██║██║                  ║
# ║             ██║╚██╔╝██║██╔══██║ ██║██║     ██║   ██║██║                  ║
# ║             ██║ ╚═╝ ██║██║  ██║ ██║███████╗╚██████╔╝╚██████╗             ║
# ║             ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═╝╚══════╝ ╚═════╝  ╚═════╝             ║
# ║                                                                          ║
# ║    Project: network_scanner v1.0.0                                       ║
# ║    Created: 2025-04-18                                                   ║
# ║    Author: ma1loc (youness anflous)                                      ║
# ║                                                                          ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import scapy.all as scapy
import	subprocess
import	sys
import	os
1
def	scan(ip):
	broadcast_mac = "ff:ff:ff:ff:ff:ff"
	arp_requst = scapy.ARP(pdst=ip)
	ether_requst = scapy.Ether(dst=broadcast_mac)
	packet = ether_requst/arp_requst

	pinging, unpinging = scapy.srp(packet, timeout=1)    # srp sends & receives packets at Layer 2
	print(pinging.summary())  
	# for sent, received in pinging:
	# 	print(f"{received.psrc} is up, MAC: {received.hwsrc}", flush=True)

	
def	main():
	scan("10.32.0.1/16")

if __name__ == "__main__":
	main()
