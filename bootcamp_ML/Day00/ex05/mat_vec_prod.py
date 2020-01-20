import numpy as np

def dot(x, y):
	"""
	Computes the dot product of two non-empty numpy.ndarray, using a for-loop. The two arrays must have the same dimensions.
	Args:
		x: has to be an numpy.ndarray, a vector.
		y: has to be an numpy.ndarray, a vector.
	Returns:
		The dot product of the two vectors as a float.
		None if x or y are empty numpy.ndarray.
		None if x and y does not share the same dimensions.
	Raises:
		This function should not raise any Exception.
	"""
	
	if not type(x) == np.ndarray or x.size < 1:
		return None
	if not type(y) == np.ndarray or y.size < 1:
		return None
	if y.size != x.size:
		return None

	result = 0
	for i, _ in np.ndenumerate(x):
		result += x[i] * y[i]
	return result


def mat_vec_prod(x, y):
	"""
	Computes the product of two non-empty numpy.ndarray, using a for-loop. The two arrays must have compatible dimensions.
	Args:
		x: has to be an numpy.ndarray, a matrix of dimension m * n.
		y: has to be an numpy.ndarray, a vector of dimension n * 1.
	Returns:
		The product of the matrix and the vector as a vector of dimension m * 1.
		None if x or y are empty numpy.ndarray.
		None if x and y does not share compatibles dimensions.
	Raises:
		This function should not raise any Exception.
	"""

	if not type(x) == np.ndarray or x.size < 1 or len(x.shape) < 2:
		return None
	if not type(y) == np.ndarray or y.size < 1 or y.shape[1] > 1:
		return None
	if y.size != x.shape[1]:
		return None
	
	result = np.array([])
	for item in x:
		result = np.append(result, dot(item, y))
	return result

def main():
	W = np.array([
	[ -8, 8, -6, 14, 14, -9, -4],
	[ 2, -11, -2, -11, 14, -2, 14],
	[-13, -2, -5, 3, -8, -4, 13],
	[ 2, 13, -14, -15, -14, -15, 13],
	[ 2, -1, 12, 3, -7, -3, -6]])
	X = np.array([0, 15, -9, 7, 12, 3, -21]).reshape((7,1))
	Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((7,1))
	print(mat_vec_prod(W, X))
	W.dot(X)
	print(mat_vec_prod(W, Y))
	W.dot(Y)

if __name__ == "__main__":
	main()