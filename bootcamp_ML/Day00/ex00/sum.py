import numpy

def sum_(x, f):
	"""
	Computes the sum of a non-empty numpy.ndarray onto wich a function is applied element-wise, using a for-loop.

	Args:
		x: has to be an numpy.ndarray, a vector.
		f: has to be a function, a function to apply element-wise to the vector.
	Returns:
		The sum as a float.
		None if x is an empty numpy.ndarray or if f is not a valid function.
	Raises:
		This function should not raise any Exception.
	"""
	if not type(x) == numpy.ndarray:
		return None
	if not callable(f) or x.size < 1:
		return None

	result = 0
	for cell in x:
		result += f(cell)
	return float(result)


def main():
	X = numpy.array([0, 15, -9, 7, 12, 3, -21])
	print(sum_(X, lambda x: x))
	X = numpy.array([0, 15, -9, 7, 12, 3, -21])
	print(sum_(X, lambda x: x**2))

if __name__ == "__main__":
	main()
