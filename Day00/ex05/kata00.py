import sys

def main():
	t = (19,42,21)
	string = ", ".join(map(str,t))
	print(f"The {len(t)} numbers are: {string}")

if __name__ == "__main__":
	main()