import sys

def print_and_quit(str):
	print(str)
	return(0)


def main():
	if (len(sys.argv) != 2 or not sys.argv[1].isnumeric()):
		return print_and_quit("ERROR")
	number = int(sys.argv[1])
	if number == 0:
		return print_and_quit("I'm Zero.")
	elif number % 2 == 0:
		return print_and_quit("I'm Even.")
	else:
		return print_and_quit("I'm Odd.")



if __name__ == '__main__':
    main()	