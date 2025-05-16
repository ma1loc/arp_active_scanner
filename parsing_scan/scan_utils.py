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

from	parsing_scan.rgb_msg import s_print
from	parsing_scan.rgb_msg import w_print
from	parsing_scan.rgb_msg import e_print
import	netifaces
import	ipaddress
import	sys
import	os

def	is_root():
	if os.geteuid() != 0:
		w_print("You must be root!!!", newline=True)
		sys.exit(1)

def	handle_sigint(signum, frame):
	s_print("\nQuit\n", newline=False)
	sys.exit(0)

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def	is_nic_up(interface):
    try:
        with open(f"/sys/class/net/{interface}/operstate") as f:
            return f.read().strip() == "up"
    except:
        return False

#  have to check if the interface is there not not
def check_interface_exists(interface):
    return os.path.exists(f"/sys/class/net/{interface}")
    
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
            e_print(f"Interface: {nic} does not have an IPv4 address")
            sys.exit(1)
    return None

def	get_addr_nic(nic):
    try:
        ipv4_info = netifaces.ifaddresses(nic)[netifaces.AF_INET][0]
        ip = ipv4_info['addr']
        netmask = ipv4_info['netmask']
        s_print("\u2B24 Active ", newline=False)
        print(f"Interface: {nic}, IP: {ip}, Netmask: {netmask}")
        network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
        return network
    except (KeyError, IndexError):
        e_print(f"Interface: {nic} does not have an IPv4 address")
        sys.exit(1)
