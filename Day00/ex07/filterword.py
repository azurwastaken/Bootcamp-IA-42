import sys
import string
import re

def args_are_valids(av):
	if len(av) != 2:
		return False
	if not (isinstance(av[0], str) and av[1].isnumeric()):
		return False
	if int(av[1]) <= 0:
		return False
	return True

def main(av):
	if not args_are_valids(av):
		print("ERROR")
		return
	a = av[0]
	n = int(av[1])
	a = a.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
	shortword = re.compile(r'\W*\b\w{1,' + str(n) +r'}\b')
	a = shortword.sub('', a)
	a = a.split()
	print(a)
	

if __name__ == "__main__":
	main(sys.argv[1:])