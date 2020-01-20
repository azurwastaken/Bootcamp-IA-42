import math
import numpy


def mean(x):
	"""Computes the mean of a non-empty numpy.ndarray, using a for-loop.
	Args:
	 x: has to be an numpy.ndarray, a vector.
	Returns:
	 The mean as a float.
	 None if x is an empty numpy.ndarray.
	Raises:
	 This function should not raise any Exception.
	"""
	if not type(x) == numpy.ndarray or x.size < 1:
		return None
	
	somme = 0
	for item in x:
		somme += item
	return float(somme / x.size)


def variance(x):
	"""Computes the variance of a non-empty numpy.ndarray, using a for-loop.
	Args:
	 x: has to be an numpy.ndarray, a vector.
	Returns:
	 The variance as a float.
	 None if x is an empty numpy.ndarray.
	Raises:
	 This function should not raise any Exception.
	"""

	if not type(x) == numpy.ndarray or x.size < 1:
		return None
	
	coef = (1/x.size)
	meanpls = mean(x)
	sumof = 0
	for item in x:
		sumof += math.pow(item - meanpls,2)
	return sumof * coef

def std(x):
	"""
	Computes the standard deviation of a non-empty numpy.ndarray, using a for-loop.
	Args:
		x: has to be an numpy.ndarray, a vector.
	Returns:
		The standard deviation as a float.
		None if x is an empty numpy.ndarray.
	Raises:
		This function should not raise any Exception.
	"""

	if not type(x) == numpy.ndarray or x.size < 1:
		return None
	return math.sqrt(variance(x))

def main():
	X = numpy.array([0, 15, -9, 7, 12, 3, -21])
	print(std(X))
	print(numpy.std(X))
	Y = numpy.array([2, 14, -13, 5, 12, 4, -19])
	print(std(Y))
	print(numpy.std(Y))

if __name__ == "__main__":
	main()