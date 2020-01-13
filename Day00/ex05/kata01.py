import sys

def main():
	languages = {
		'Python': 'Guido van Rossum',
		'Ruby': 'Yukihiro Matsumoto',
		'PHP': 'Rasmus Lerdorf',
	}
	for name in languages:
		print(f"{name} was created by {languages[name]}")

if __name__ == "__main__":
	main()