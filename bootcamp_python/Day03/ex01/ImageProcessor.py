import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os.path

class ImageProcessor:
	def __init__(self):
		pass

	@staticmethod
	def load(path):
		if not isinstance(path, str):
			raise ValueError("Path should be a string")
		if not os.path.exists(path):
			raise Exception(f"{path} doesn't exist")
		img = mpimg.imread(path)
		print(f"Loading image of dimensions {len(img[0])}x{len(img)}")
		return(img)
	
	@staticmethod
	def display(img):
		plt.imshow(img)
		plt.show()

