import sys
import string

def text_analyzer(text = ""):
	"""
	This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
	"""
	if not text:
		text = input("Please prompt a text to analyze\n")
	print(f"the text contains {len(text)} character(s):")
	print(f"- {sum(1 for c in text if c.isupper())} uppers letter(s)")
	print(f"- {sum(1 for c in text if c.islower())} lower letter(s)")
	print(f"- {sum(map(text.count, set(string.punctuation)))} punctuation mark(s)")
	print(f"- {text.count(' ')} space(s)")
	

def main(argv):
	try:
		text_analyzer(argv[0])
	except:
		text_analyzer()


if __name__ == '__main__':
    main(sys.argv[1:])	