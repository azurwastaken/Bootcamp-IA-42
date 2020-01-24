import numpy as np

def predict_(theta, X):
    """
    Description:
    Prediction of output using the hypothesis function (linear model).
    For example in linear regression, hypothesis is the line between all the dot
    Args:
    theta: has to be a numpy.ndarray, a vector of dimension (number of features + 1, 1).
    X: has to be a numpy.ndarray, a matrix of dimension (number of training examples, number of features).
    Returns:
    pred: numpy.ndarray, a vector of dimension (number of the training examples,1).
    None if X does not match the dimension of theta.
    Raises:
    This function should not raise any Exception.
    """
    m = len(X)
    X = np.append(np.full((m, 1), fill_value=1), X, axis = 1)
    return X.dot(theta)

def main():
    X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
    theta1 = np.array([[2.], [4.]])
    print(predict_(theta1, X1))
    print("expected[[2], [6], [10], [14.], [18.]]")
    X3 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8.,80.]])
    theta3 = np.array([[0.05], [1.], [1.], [1.]])
    print(predict_(theta3, X3))
    print("Expected [[22.25], [44.45], [66.65], [88.85]]")

if __name__ == "__main__":
    # execute only if run as a script
    main()