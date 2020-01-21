import numpy as np

class MyLinearRegression():
	"""
	Description:
		My personnal linear regression class to fit like a boss.
"""
	def __init__(self, theta):
		"""
		Description:
			generator of the class, initialize self.
		Args:
			theta: has to be a list or a numpy array, it is a vector of dimension (number of features + 1, 1).
		Raises:
			This method should noot raise any Exception.
		"""
		self.theta = theta
	
	def predict_(self, X):
		
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
			predicted = np.dot(arranged_X, self.theta)
		except:
			return None
		return predicted
	
	def cost_elem_(self, X, Y):
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
		y_hat = self.predict_(X)
		for i in range(M):
			J[i] = pow(y_hat[i] - Y[i], 2) * (0.5/M)
		return J
	
	def cost_(self, X, Y):
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
		return np.sum(self.cost_elem_(X, Y))
	
	def fit_(self, X, Y, alpha=0.1, n_cycle=1000):
		m = len(Y)
		thetatmp = self.theta
  		line_of_1 = np.full((np.shape(X)[0], 1), fill_value=1)
		X = np.append(line_of_1, X, axis=1)
		for i in range(n_cycle):
			prediction = np.dot(X,theta)
			thetatmp = thetatmp -(1/m)*alpha*( X.T.dot((prediction - Y)))
			
		return thetatmp