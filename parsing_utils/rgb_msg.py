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

# rgb_msg.py

def e_print(msg, newline):
    RED = "\033[91m"
    RESET = "\033[0m"
    if newline:
        print(f"{RED}{msg}{RESET}")
    else:
        print(f"{RED}{msg}{RESET}", end="")

def s_print(msg, newline):
    GREEN = "\033[92m"
    RESET = "\033[0m"
    if newline:
        print(f"{GREEN}{msg}{RESET}")
    else:
        print(f"{GREEN}{msg}{RESET}", end="")

def w_print(msg, newline):
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    if newline:
        print(f"{YELLOW}{msg}{RESET}")
    else:
        print(f"{YELLOW}{msg}{RESET}", end="")

