import numpy as np


def mat_mat_prod(x, y):
    """Computes the product of two non-empty numpy.ndarray, using a
for-loop. The two arrays must have compatible dimensions.
    Args:
     x: has to be an numpy.ndarray, a matrix of dimension m * n.
     y: has to be an numpy.ndarray, a vector of dimension n * p.
    Returns:
     The product of the matrices as a matrix of dimension m * p.
     None if x or y are empty numpy.ndarray.
     None if x and y does not share compatibles dimensions.
    Raises:
     This function should not raise any Exception.
    """

    res = [[0 for x in range(len(x))] for y in range(len(y[0]))]
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                print(res[i][j])
                res[i][j] += x[i][k] * y[k][j]
    return np.array(res)


if __name__ == "__main__":
    W = np.array([
        [-8, 8, -6, 14, 14, -9, -4],
        [2, -11, -2, -11, 14, -2, 14],
        [-13, -2, -5, 3, -8, -4, 13],
        [2, 13, -14, -15, -14, -15, 13],
        [2, -1, 12, 3, -7, -3, -6]])
    Z = np.array([
        [-6, -1, -8, 7, -8],
        [7, 4, 0, -10, -10],
        [7, -13, 2, 2, -11],
        [3, 14, 7, 7, -4],
        [-1, -3, -8, -4, -14],
        [9, -14, 9, 12, -7],
        [-9, -4, -10, -3, 6]])
    print(mat_mat_prod(W, Z))
    # array([[45, 414, -3, -202, -163],
    #    [-294, -244, -367, -79, 62],
    #    [-107, 140, 13, -115, 385],
    #    [-302, 222, -302, -412, 447],
    #    [108, -33, 118, 79, -67]])
    print(W.dot(Z))
    # array([[45, 414, -3, -202, -163],
    #    [-294, -244, -367, -79, 62],
    #    [-107, 140, 13, -115, 385],
    #    [-302, 222, -302, -412, 447],
    #    [108, -33, 118, 79, -67]])
    print(mat_mat_prod(Z, W))
    # array([[148, 78, -116, -226, -76,
    #     7, 45],
    #    [-88, -108, -30, 174, 364, 109, -42],
    #    [-126, 232, -186, 184, -51, -42, -92],
    #    [-81, -49, -227, -208, 112, -176, 390],
    #    [70,    3, -60, 13, 162, 149, -110],
    #    [-207, 371, -323, 106, -261, -248, 83],
    #    [200, -53, 226, -49, -102, 156, -225]])
    print(Z.dot(W))
    # array([[148, 78, -116, -226, -76,    7, 45],
    #    [-88, -108, -30, 174, 364, 109, -42],
    #    [-126, 232, -186, 184, -51, -42, -92],
    #    [-81, -49, -227, -208, 112, -176, 390],
    #    [70,    3, -60, 13, 162, 149, -110],
    #    [-207, 371, -323, 106, -261, -248, 83],
    #    [200, -53, 226, -49, -102, 156, -225]])