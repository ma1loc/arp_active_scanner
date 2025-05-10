import	os

def	check_is_root():
	id = os.geteuid()
	if (id != 0):
		print("Your must be a root.")
		exit(1)

# check if the interface if there