import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class ColorFilter:
	def __init__(self):
		pass

	@staticmethod
	def invert(array):

	@staticmethod
	def to_blue(array):
		pic = array
		fig, ax = plt.subplots(nrows = 1, ncols=3, figsize=(15,5))
		for c, ax in zip(range(3), ax):
			# create zero matrix
			split_img = np.zeros(pic.shape) # 'dtype' by default: 'numpy.float64'
			# assing each channel
			split_img[ :, :, c] = pic[ :, :, c]
			# display each channel
			ax.imshow(split_img)

	@staticmethod
	def to_green(array):

	@staticmethod
	def to_red(array):

	@staticmethod
	def celluloid(array):