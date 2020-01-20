import sys

def add(a, b):
	a = int(a)
	b = int(b)
	return a + b


def sub(a, b):
	a = int(a)
	b = int(b)
	return a - b


def mult(a, b):
	a = int(a)
	b = int(b)
	return a * b			


def div(a, b):
	a = int(a)
	b = int(b)
	if b == 0:
		return "ERROR (div by 0)"
	return a / b			


def mod(a, b):
	a = int(a)
	b = int(b)
	if b == 0:
		return "ERROR (modulo by 0)"
	return a % b			


def main(av):
	if len(av) == 0:
		print("Usage: python operations.py\n\n"
		"Example:\n"
    	"python operations.py 10 3")
		return
	elif len(av) > 2:
		print("InputError: too many arguments")
		return 0
	elif not av[0].isnumeric() or not av[1].isnumeric():
		print("InputError: only numbers")
		return 0
	print(f"{'Sum:'.ljust(20)} {add(av[0],av[1])}")
	print(f"{'Difference:'.ljust(20)} {sub(av[0],av[1])}")
	print(f"{'Product:'.ljust(20)} {mult(av[0],av[1])}")
	print(f"{'Quotient:'.ljust(20)} {div(av[0],av[1])}")
	print(f"{'Remainder:'.ljust(20)} {mod(av[0],av[1])}")
	

if __name__ == '__main__':
    main(sys.argv[1:])	