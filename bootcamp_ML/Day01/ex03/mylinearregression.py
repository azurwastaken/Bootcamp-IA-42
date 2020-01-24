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
    theta: has to be a list or a numpy array, it is a vector of
    dimension (number of features + 1, 1).
    Raises:
    This method should noot raise any Exception.
    """
    self.theta = theta

def predict_(self, X):
    m = len(X)
    X = np.append(np.full((m, 1), fill_value=1), X, axis = 1)
    return X.dot(self.theta)

def cost_elem_(self, X, Y):
    m = len(X)
    X = np.append(np.full((m, 1), fill_value=1), X, axis = 1)
    hypothesis = X.dot(self.theta)

    return np.power(np.subtract(hypothesis, Y), 2) * (1/(2 * m))


def cost_(self, X, Y):
    m = len(X)
    X = np.append(np.full((m, 1), fill_value=1), X, axis = 1)
    hypothesis = X.dot(self.theta)

    return np.sum(np.power(np.subtract(hypothesis, Y), 2) * (1/(2 * m)))

def fit_(self, X, Y, learning_rate = 0.001, n_cycle = 10000):
    m = len(X)
    for _ in range(n_cycle):
        X_with_Xzero = np.append(np.full((m, 1), fill_value=1), X, axis = 1)
        hypothesis = X_with_Xzero.dot(self.theta)
        parenthesis = np.subtract(hypothesis, Y)
        sigma = np.sum(np.dot(X_with_Xzero.T,parenthesis),keepdims=True, axis=1)
        subtract_elem_snd = learning_rate * (0.5 / m) * sigma
        self.theta = self.theta - subtract_elem_snd