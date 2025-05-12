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

# import scapy.all as scapy
# import sys
# import os

# def scan(ip_range):
#     broadcast_mac = "ff:ff:ff:ff:ff:ff"
#     for i in range(1, 255):  # Scan IPs from .1 to .254
#         ip = f"{ip_range}.{i}"
#         arp_request = scapy.ARP(pdst=ip)
#         ether_request = scapy.Ether(dst=broadcast_mac)
#         packet = ether_request / arp_request

#         answered = scapy.srp(packet, timeout=1, verbose=0)[0]
#         for sent, received in answered:
#             print(f"{received.psrc} is up, MAC: {received.hwsrc}", flush=True)

# def main():
#     if os.geteuid() != 0:
#         sys.exit("Run as root: sudo python3 setup.py")
#     scan("10.32.1")

# if __name__ == "__main__":
#     main()

# // what is it for?
#  for nic in interfaces:
#         if nic == "lo":
#             continue

# import netifaces
# import scapy.all as scapy

# def is_nic_up(interface):
#     try:
#         with open(f"/sys/class/net/{interface}/operstate") as f:
#             return f.read().strip() == "up"
#     except FileNotFoundError:
#         return False

# def s_print(msg, newline=True):
#     GREEN = "\033[92m"
#     RESET = "\033[0m"
#     if newline:
#         print(f"{GREEN}{msg}{RESET}")
#     else:
#         print(f"{GREEN}{msg}{RESET}", end="")

# def get_active_nic():
#     interfaces = netifaces.interfaces()
#     for nic in interfaces:
#         if nic == "lo" or not is_nic_up(nic):
#             continue
#         try:
#             ipv4_info = netifaces.ifaddresses(nic)[netifaces.AF_INET][0]
#             ip = ipv4_info['addr']
#             netmask = ipv4_info['netmask']
#             s_print("Active ", newline=False)
#             print(f"Interface: {nic}, IP: {ip}, Netmask: {netmask}")
#         except (KeyError, IndexError):
#             print(f"Interface: {nic} does not have an IPv4 address")

# def arp_scan(ip):
#     broadcast_mac = "ff:ff:ff:ff:ff:ff"
#     broadcast_ether = scapy.Ether(dst=broadcast_mac)
#     arp_request = scapy.ARP(pdst=ip)
#     packet = broadcast_ether / arp_request
#     answered, _ = scapy.srp(packet, timeout=1, verbose=False)

#     print("IP Address\t\tMAC Address\n" + "-" * 40)
#     for _, received_packet in answered:
#         print(f"{received_packet.psrc}\t\t{received_packet.hwsrc}")

# def main():
#     get_active_nic()
#     # arp_scan("10.32.86.170/21")

# if __name__ == "__main__":
#     main()


