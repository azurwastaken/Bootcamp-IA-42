import numpy as np
from math import pow

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

def cost_elem_(theta, X, Y):
	"""
	Description:
		Calculates all the elements (0.5/M) * (y_pred - y)^2 of the cost function.
	Args:
		theta: has to be a numpy.ndarray, a vector of dimension (number of features + 1, 1).
		X: has to be a numpy.ndarray, a matrix of dimension (number of training examples, number of features).
	Returns:
		J_elem: numpy.ndarray, a vector of dimension (number of the training examples,1).
		None if there is a dimension matching problem between X, Y or theta.
	Raises:
		This function should not raise any Exception.
	"""
 
	M = len(X)
	J = np.zeros((X.shape[0],1))
	y_hat = predict_(theta, X)
	for i in range(M):
		J[i] = pow(y_hat[i] - Y[i], 2) * (0.5/M)
	return J
	





def cost_(theta, X, Y):
	"""
	Description:
		Calculates the value of cost function.
	Args:
		theta: has to be a numpy.ndarray, a vector of dimension (number of features + 1, 1).
		X: has to be a numpy.ndarray, a vector of dimension (number of training examples, number of features).
	Returns:
		J_value : has to be a float.
		None if X does not match the dimension of theta.
		Raises:
		This function should not raise any Exception.
	"""
	return np.sum(cost_elem_(theta, X, Y))

def main():
	X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
	theta1 = np.array([[2.], [4.]])
	Y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
	print(cost_elem_(theta1, X1, Y1))
	print(cost_(theta1, X1, Y1))
	X2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8.,80.]])
	theta2 = np.array([[0.05], [1.], [1.], [1.]])
	Y2 = np.array([[19.], [42.], [67.], [93.]])
	print(cost_elem_(theta2, X2, Y2))
	print(cost_(theta2, X2, Y2))

if __name__ == "__main__":
	main()