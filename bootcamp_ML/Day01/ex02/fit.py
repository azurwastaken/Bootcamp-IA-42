import numpy as np

def fit_(theta, X, Y, learning_rate = 0.001, n_cycle = 10000):
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
    m = len(X)
    for _ in range(n_cycle):
        X_with_Xzero = np.append(np.full((m, 1), fill_value=1), X, axis = 1)
        hypothesis = X_with_Xzero.dot(theta)
        parenthesis = np.subtract(hypothesis, Y)
        sigma = np.sum(np.dot(X_with_Xzero.T,parenthesis),keepdims=True, axis=1)
        subtract_elem_snd = learning_rate * (0.5 / m) * sigma
        theta = theta - subtract_elem_snd
    return theta

def main():
    X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
    Y1 = np.array([[2.], [6.], [10.], [14.], [18.]])
    theta1 = np.array([[1.], [1.]])
    theta1 = fit_(theta1, X1, Y1, learning_rate = 0.01, n_cycle=2000)
    print(theta1)
    X2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8.,80.]])
    Y2 = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
    theta2 = np.array([[42.], [1.], [1.], [1.]])
    theta2 = fit_(theta2, X2, Y2, learning_rate = 0.0005, n_cycle=42000)
    print(theta2)

if __name__ == "__main__":
    main()
        
    
