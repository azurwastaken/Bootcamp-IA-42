import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class ColorFilter:
	def __init__(self):
		pass

	@staticmethod
	def invert(array):
		return 1 - array

	@staticmethod
	def to_blue(array):
		pic = array
		fig, ax = plt.subplots(nrows = 1, ncols=3, figsize=(15,5))
		# create zero matrix
		split_img = np.zeros(pic.shape) # 'dtype' by default: 'numpy.float64'
		# assing each channel
		split_img[ :, :, 2] = pic[ :, :, 2]
		# display each channel
		return split_img

	@staticmethod
	def to_green(array):
		def to_green(self, array):
        greened = array
        greened[:, :, 2] *= 0.0
        greened[:, :, 0] *= 0.0
        return greened

	@staticmethod
	def to_red(array):
        rededredemption = array
        rededredemption -= to_blue(array)
        rededredemption -= to_green(array)
        return rededredemption

	@staticmethod
	def celluloid(array):