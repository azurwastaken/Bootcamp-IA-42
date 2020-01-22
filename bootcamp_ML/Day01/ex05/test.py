import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from mylinearregression import MyLinearRegression as MyLR
from linear_model import plot_model, plot_cost_fct_byTheta


CSV_FILE = '/Users/mcaseaux/github_perso/Bootcamp-IA-42/bootcamp_ML/Day01/resources/spacecraft_data.csv'

if __name__ == "__main__":
	data = pd.read_csv(CSV_FILE)
	Y = np.array(data["Sell_price"])
	X = np.array(data[["Age","Thrust_power","Terameters"]])
	models = MyLR(([0.0],[0.0],[0.0],[0.0]))
	print(models.theta)
	models.fit_(X,Y, alpha=1e-4, n_cycle=60000)
	print(models.theta)
	plot_model(np.transpose(X)[0], Y, models.predict_(X))
		