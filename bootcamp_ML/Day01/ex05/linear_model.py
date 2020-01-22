 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_cost_fct_byTheta(model, X, Y, id_thet):
    min_val = model.theta[id_thet]
    cost_fct = []
    range_value = np.arange(min_val - 50, min_val + 50, 0.1)
    for i in range_value:
        model.theta[id_thet] = i
        cost_fct.append(model.cost_(X, Y))
    plt.plot(list(range_value),cost_fct)
    plt.show()
    model.theta[id_thet] = min_val

def plot_model(X, Y, models):
	plt.scatter(X, Y, color="g")
	plt.xlabel("Quantity of bluepill")
	plt.ylabel("Space driving score")
	plt.plot(X, models, color="blue", label="menfou")
	plt.legend()
	plt.show()