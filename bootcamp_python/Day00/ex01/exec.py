import sys

def main():
	#Get Argv and delete the first elem (file name)
	sentence = sys.argv
	del sentence[0]
	#Convert list into string
	sentence = " ".join(sentence)
	#Use Case swap on the sentence
	sentence = sentence.swapcase()
	#Print the string reverted
	print(sentence[::-1])

if __name__ == '__main__':
    main()	