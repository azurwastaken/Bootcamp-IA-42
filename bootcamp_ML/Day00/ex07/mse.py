import numpy as np
from math import pow

def mse(y, y_hat):
	"""
	Computes the mean squared error of two non-empty numpy.ndarray, using a for-loop. The two arrays must have the same dimensions.
	Args:
		y: has to be an numpy.ndarray, a vector.
		y_hat: has to be an numpy.ndarray, a vector.
	Returns:
		The mean squared error of the two vectors as a float.
		None if y or y_hat are empty numpy.ndarray.
		None if y and y_hat does not share the same dimensions.
	Raises:
		This function should not raise any Exception.
	"""

	if not type(y_hat) == np.ndarray or y_hat.size < 1 or len(y_hat.shape) > 1:
		return None
	if not type(y) == np.ndarray or y.size < 1 or len(y.shape) > 1:
		return None
	if y.size != y_hat.size:
		return None
	
	coef = (1 / y.size)
	result = 0
	for i, _ in np.ndenumerate(y):
		result += pow(y[i] - y_hat[i], 2)
	return coef * result


def main():
	X = np.array([0, 15, -9, 7, 12, 3, -21])
	Y = np.array([2, 14, -13, 5, 12, 4, -19])
	print(mse(X, Y))
	print(mse(X, X))

if __name__ == "__main__":
	main()