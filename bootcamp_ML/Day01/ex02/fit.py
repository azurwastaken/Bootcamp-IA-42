import numpy as np


def vec_gradient(x, y, theta):
	"""
	Computes a gradient vector from three non-empty numpy.ndarray, without any for-loop. The three arrays must have the compatible dimensions.
	Args:
		x: has to be an numpy.ndarray, a matrice of dimension m * n.
		y: has to be an numpy.ndarray, a vector of dimension m * 1.
		theta: has to be an numpy.ndarray, a vector n * 1.
	Returns:
		The gradient as a numpy.ndarray, a vector of dimensions n * 1, containg the result of the formula for all j.
		None if x, y, or theta are empty numpy.ndarray.
		None if x, y and theta do not have compatible dimensions.
	Raises:
		This function should not raise any Exception.
	"""
	parenthesis = np.subtract(x.dot(theta), y)
	coef = x.dot(1/x.shape[0])
	return np.transpose(coef).dot(parenthesis)

def predict_(theta, X):
	"""
	Description:
		Prediction of output using the hypothesis function (linear model).
	Args:
		theta: has to be a numpy.ndarray, a vector of dimension (number of features + 1, 1).
		X: has to be a numpy.ndarray, a matrix of dimension (number of training examples, number of features).
	Returns:
		pred: numpy.ndarray, a vector of dimension (number of the training examples,1).
		None if X does not match the dimension of theta.
	Raises:
		This function should not raise any Exception.
	"""
	line_of_1 = np.full((np.shape(X)[0], 1), fill_value=1)
	arranged_X = np.append(line_of_1, X, axis=1)
	try:
		predicted = np.dot(arranged_X, theta)
	except:
		return None
	return predicted

def fit_(theta, X, Y, alpha=0.1, n_cycle=1000):
	"""
	Description:
		Performs a fit of Y(output) with respect to X.
	Args:
		theta: has to be a numpy.ndarray, a vector of dimension (number of features + 1, 1).
		X: has to be a numpy.ndarray, a matrix of dimension (number of training examples, number of features).
		Y: has to be a numpy.ndarray, a vector of dimension (number of training examples, 1).
	Returns:
		new_theta: numpy.ndarray, a vector of dimension (number of the features +1,1).
		None if there is a matching dimension problem.
	Raises:
		This function should not raise any Exception.
	"""
 
	m = len(Y)
	line_of_1 = np.full((np.shape(X)[0], 1), fill_value=1)
	X = np.append(line_of_1, X, axis=1)
	for i in range(n_cycle):
		prediction = np.dot(X,theta)
		theta = theta -(1/m)*alpha*( X.T.dot((prediction - Y)))
		
	return theta

def main():
	X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
	Y1 = np.array([[2.], [6.], [10.], [14.], [18.]])
	theta1 = np.array([[1.], [1.]])
	theta1 = fit_(theta1, X1, Y1, alpha = 0.01, n_cycle=2000)
	print("theta1")
	print(theta1)
	print(predict_(theta1, X1))
	X2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8.,80.]])
	Y2 = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
	theta2 = np.array([[42.], [1.], [1.], [1.]])
	theta2 = fit_(theta2, X2, Y2, alpha = 0.0005, n_cycle=42000)
	print("theta2")
	print(theta2)
	print(predict_(theta2, X2))

if __name__ == '__main__':
	main()
	