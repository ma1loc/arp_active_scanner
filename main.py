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

import	scapy.all as scapy
import	ipaddress
from	parsing_utils.rgb_msg import s_print
import	time
import	ipaddress
import	netifaces
import	sys

def	is_nic_up(interface):
    try:
        with open(f"/sys/class/net/{interface}/operstate") as f:
            return f.read().strip() == "up"
    except:
        return False

def get_active_nic():
    interfaces = netifaces.interfaces()
    for nic in interfaces:
        if nic == "lo" or not is_nic_up(nic):
            continue
        try:
            ipv4_info = netifaces.ifaddresses(nic)[netifaces.AF_INET][0]
            ip = ipv4_info['addr']
            netmask = ipv4_info['netmask']
            s_print("\u2B24 Active ", newline=False)
            print(f"Interface: {nic}, IP: {ip}, Netmask: {netmask}")
            network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
            return network
        except (KeyError, IndexError):
            print(f"Interface: {nic} does not have an IPv4 address")
    return None


def arp_scan(ip):
    broadcast_mac = "ff:ff:ff:ff:ff:ff"
    broadcast_ether = scapy.Ether(dst=broadcast_mac)
    arp_request = scapy.ARP(pdst=ip)
    packet = broadcast_ether / arp_request

    print("IP Address\t\tMAC Address")
    print("-" * 40)
    queried_ips = set()

    while True:
        answered, unanswered = scapy.srp(packet, timeout=1, verbose=False)
        if answered:
            for send_packet, received_packet in answered:
                ip = received_packet.psrc
                if ip not in queried_ips:
                    print(f"{ip}\t\t{received_packet.hwsrc}")
                    queried_ips.add(ip)
                time.sleep(0.5)
        else:
            break

import	os

def clear_terminal():
    # Clear the terminal screen
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear_terminal()
    network = get_active_nic()
    if network:
        arp_scan(str(network))

if __name__ == "__main__":
	main()
