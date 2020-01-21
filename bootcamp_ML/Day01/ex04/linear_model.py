 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_model(X, Y, models):
	plt.scatter(X, Y, color="g")
	plt.xlabel("Quantity of bluepill")
	plt.ylabel("Space driving score")
	plt.plot(X, models, color="blue", label="menfou")
	plt.legend()
	plt.show()