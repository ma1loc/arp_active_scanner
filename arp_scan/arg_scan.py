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

from mac_vendor_lookup import MacLookup
import scapy.all as scapy
import ipaddress
import random
import time

1
def arp_scan(ip_range, stealth):
    print("IP Address\t\tMAC Address\t\t\tVendor")
    print("-" * 75)
    queried_ips = set()
    mac_lookup = MacLookup()

    if stealth:
        # stealth Mode: one-by-one scan with random delay
        network = ipaddress.IPv4Network(ip_range, strict=False)
        for ip in network.hosts():
            packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=str(ip))
            answered, _ = scapy.srp(packet, timeout=1, verbose=False)
            for _, received in answered:
                ip = received.psrc
                if ip not in queried_ips:
                    mac = received.hwsrc
                    try:
                        vendor = mac_lookup.lookup(mac)
                    except:
                        vendor = "Unknown"
                    print(f"{ip}\t\t{mac}\t\t{vendor}")
                    queried_ips.add(ip)
            time.sleep(random.uniform(0.8, 1.5))  # random delay
    else:
        # fast mode
        broadcast_mac = "ff:ff:ff:ff:ff:ff"
        broadcast_ether = scapy.Ether(dst=broadcast_mac)
        arp_request = scapy.ARP(pdst=ip_range)
        packet = broadcast_ether / arp_request
        while True:
            answered, _ = scapy.srp(packet, timeout=1, verbose=False)
            if answered:
                for _, received in answered:
                    ip = received.psrc
                    if ip not in queried_ips:
                        mac = received.hwsrc
                        try:
                            vendor = mac_lookup.lookup(mac)
                        except:
                            vendor = "Unknown"
                        print(f"{ip}\t\t{mac}\t\t{vendor}")
                        queried_ips.add(ip)
                    time.sleep(0.5)
            time.sleep(1)