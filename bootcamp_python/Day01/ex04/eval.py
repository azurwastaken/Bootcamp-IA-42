class Evaluator:
	@classmethod
	def zip_evaluate(self, coefs, words):
		if len(coefs) != len(words):
			return -1
		zucced = zip(words, coefs)
		result = 0
		for couple in zucced:
			result += len(couple[0]) * couple[1]
		print(result)

	@classmethod
	def enumerate_evaluate(self, coefs, words):
		if len(coefs) != len(words):
			return -1
		result = 0
		for i, word in enumerate(words):
			result += len(word) * coefs[i]
		print(result)


def main():
	words = ["Le", "Lorem", "Ipsum", "est", "simple"]
	coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
	Evaluator.enumerate_evaluate(coefs, words)

if __name__ == "__main__":
	main()