import numpy as np

def linear_mse(x, y, theta):
	"""
	Computes the mean squared error of three non-empty numpy.ndarray, using a for-loop. The three arrays must have compatible dimensions.
	Args:
		y: has to be an numpy.ndarray, a vector of dimension m * 1.
		x: has to be an numpy.ndarray, a matrix of dimesion m * n.
		theta: has to be an numpy.ndarray, a vector of dimension n * 1.
	Returns:
		The mean squared error as a float.
		None if y, x, or theta are empty numpy.ndarray.
		None if y, x or theta does not share compatibles dimensions.
	Raises:
		This function should not raise any Exception.
	"""
	if not type(x) == np.ndarray or x.size < 1 or len(x.shape) < 2:
		return None
	if not type(y) == np.ndarray or y.size < 1 or len(y.shape) > 1:
		return None
	if not type(theta) == np.ndarray or theta.size < 1 or len(theta.shape) > 1:
		return None
	if y.size != x.shape[0] or theta.size != x.shape[1]:
		return None
	

	ret = 0
	for i in range(len(y)):
		hx = np.dot(theta, x[i])
		hxy = hx - y[i]
		ret += hxy**2
	return ret / len(x)