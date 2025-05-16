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
from parsing_scan.scan_utils import handle_sigint
signal.signal(signal.SIGINT, handle_sigint)
from parsing_scan.scan_utils import is_root
from parsing_scan.scan_utils import clear_terminal
from parsing_scan.scan_utils import get_active_nic
from parsing_scan.parsing import input_parsing
from arp_scan.arg_scan import arp_scan
from parsing_scan.rgb_msg import e_print
from parsing_scan.rgb_msg import w_print
from parsing_scan.scan_utils import check_interface_exists
from parsing_scan.scan_utils import is_nic_up
from parsing_scan.scan_utils import get_addr_nic

def main():
    is_root()
    user_args = input_parsing()

    if user_args.interface:
        clear_terminal()
        if check_interface_exists(user_args.interface) and is_nic_up(user_args.interface):
            network = get_addr_nic(user_args.interface)
            if user_args.fast_scan:
                arp_scan(str(network), stealth=False)
            elif user_args.stealth:
                arp_scan(str(network), stealth=True)
            else:
                w_print("No scan mode selected, defaulting to stealth mode...", newline=True)
                arp_scan(str(network), stealth=True)
        else:
            e_print(f"{user_args.interface}: Down OR No such device exists", newline=True)
    else:
        network = get_active_nic()
        if network:
            clear_terminal()
            arp_scan(str(network), stealth=False)

if __name__ == "__main__":
    main()
