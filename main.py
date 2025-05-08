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

def	arp_scan(ip):
	broadcast_mac = "ff:ff:ff:ff:ff:ff"
	broadcast_ether = scapy.Ether(dst=broadcast_mac)
	arp_request = scapy.ARP(pdst=ip)
	packet = broadcast_ether/arp_request
	answered, unanswered = scapy.srp(packet, timeout=1, verbose=False)
	# print(answered)
	for	send_packet, received_packet in answered:
		print(f"packet ansered -> {answered}\n")


def	main():
	arp_scan("10.30.0.1")

if __name__ == "__main__":
	main()