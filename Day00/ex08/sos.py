import sys

MORSE_DICT = {
	"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
	"g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
	"m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
	"s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
	"y": "-.--", "z": "--..", "0": "-----", "1": ".----", "2": "..---",
	"3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
	"8": "---..", "9": "----."
}

def main(av):
	av = " ".join(av)
	av = av.split()

	for word in av:
		if not word.isalnum():
			print("ERROR")
			return
	av = " ".join(av)
	av = av.lower()
	av = av.replace(" ", " / ")
	for letter in MORSE_DICT:
		av = av.replace(letter, " " + MORSE_DICT[letter] + " ")	
	av = av.strip()
	print(av)

if __name__ == "__main__":
	main(sys.argv[1:])