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

import	argparse

def	input_parsing():
	parser = argparse.ArgumentParser(description="arp active scanner")

	parser.add_argument("-i", "--interface", required=False, help="interface to scan from it")
	
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-f", "--fast_scan", action="store_true" ,help="fast scaning mode: fast scaning but noisey in the network")
	group.add_argument("-s", "--stealth", action="store_true", help="stealth mode: one-by-one scan with a random delay")

	return parser.parse_args()
