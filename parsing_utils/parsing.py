from	parsing_utils.rgb_msg import s_print
from	parsing_utils.rgb_msg import w_print
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
    # Clear the terminal screen
    os.system("cls" if os.name == "nt" else "clear")
