import sys

# Args length
args_len = len(sys.argv) - 1

# Function
# try:
# 	if args_len == 0:
# 		print("")
# 		sys.exit(0)
# 	elif args_len > 1:
# 		print("AssertionError: more than one argument is provided")
# 		sys.exit(0)
# 	args = sys.argv[1]
# 	args_number = int(args)
# 	if args_number % 2 == 0:
# 		print("I'm Even.")
# 	else:
# 		print("I'm Odd.")
# except ValueError:
# 	print("AssertionError: argument is not an integer")

# another method
# Access command-line arguments
args_len = len(sys.argv) - 1

if args_len == 0:
    print("")
    sys.exit(0)

try:
    assert args_len == 1, "more than one argument is provided"
    args = sys.argv[1]
    args_number = int(args)
    if args_number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as msg:
    print("AssertionError:" + str(msg))
except ValueError:
    print("AssertionError: argument is not an integer")
