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

import signal
from parsing_utils.parsing import handle_sigint
signal.signal(signal.SIGINT, handle_sigint)
from parsing_utils.rgb_msg import s_print
from parsing_utils.parsing import is_root
from parsing_utils.parsing import clear_terminal
import scapy.all as scapy
import ipaddress
import time
import ipaddress
import netifaces
# from mac_vendor_lookup import MacLookup
from mac_vendor_lookup import MacLookup # type: ignore

print(MacLookup().lookup("00:80:41:12:FE"))
import os

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

def arp_scan(ip_range):
    broadcast_mac = "ff:ff:ff:ff:ff:ff"
    broadcast_ether = scapy.Ether(dst=broadcast_mac)
    arp_request = scapy.ARP(pdst=ip_range)
    packet = broadcast_ether / arp_request

    print("IP Address\t\tMAC Address\t\t\tVendor")
    print("-" * 75)
    queried_ips = set()

    while True:
        answered, unanswered = scapy.srp(packet, timeout=1, verbose=False)
        if answered:
            for send_packet, received_packet in answered:
                ip = received_packet.psrc
                if ip not in queried_ips:
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # print(f"{ip}\t\t{received_packet.hwsrc}")
                    mac = received_packet.hwsrc
                    try:
                        vendor = MacLookup().lookup(mac)
                    except:
                        vendor = "Unknown"
                    print(f"{ip}\t\t{mac}\t\t{vendor}")
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    queried_ips.add(ip)
                time.sleep(0.5)
            else:
                s_print("\nScan complete.\n", newline=True)
                break

def main():
    is_root()
    clear_terminal()
    network = get_active_nic()
    if network:
        arp_scan(str(network))

if __name__ == "__main__":
	main()
