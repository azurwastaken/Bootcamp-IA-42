import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from mylinearregression import MyLinearRegression as MyLR
from linear_model import plot_model


CSV_FILE = '../resources/are_blue_pills_magics.csv'

if __name__ == "__main__":
    data = pd.read_csv(CSV_FILE)
    Xpill = np.array(data['Micrograms']).reshape(-1, 1)
    Yscore = np.array(data['Score']).reshape(-1, 1)

    linear_model1 = MyLR(np.array([[89.0], [-8]]))
    linear_model2 = MyLR(np.array([[89.0], [-6]]))
    linear_model_trained = MyLR(np.array([[0.0], [0.0]]))
    Y_model1 = linear_model1.predict_(Xpill)
    Y_model2 = linear_model2.predict_(Xpill)

    linear_model_trained.fit_(Xpill, Yscore, alpha=0.01, n_cycle=100000)
    Y_model_trained = linear_model_trained.predict_(Xpill)

    print(linear_model1.mse_(Yscore, Y_model1))  # 57.60304285714282
    print(mean_squared_error(Yscore, Y_model1))  # 57.603042857142825
    plot_model(Xpill, Yscore, Y_model1)
    print(linear_model2.mse_(Yscore, Y_model2))  # 232.16344285714285
    print(mean_squared_error(Yscore, Y_model2))  # 232.16344285714285
    plot_model(Xpill, Yscore, Y_model2)
    print(linear_model2.mse_(Yscore, Y_model_trained))  # 232.16344285714285
    print(mean_squared_error(Yscore, Y_model_trained))  # 232.16344285714285
    plot_model(Xpill, Yscore, Y_model_trained)