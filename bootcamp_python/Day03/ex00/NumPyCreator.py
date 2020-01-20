import numpy as np


class NumPyCreator:
	def __init__(self):
		pass

	@staticmethod
	def from_list(lst):
		if isinstance(lst, list):
			return np.array(lst)
		raise ValueError("from_list(lst) require a list as parameter")

	@staticmethod
	def from_tuple(tpl):
		if isinstance(tpl, tuple):
			return np.array(tpl)
		raise ValueError("from_list(lst) require a list as parameter")

	@staticmethod
	def from_iterable(iterable):
		return np.fromiter(iterable, int)

	@staticmethod
	def from_shape(shape,value=0):
		if isinstance(shape, int) or (isinstance(shape, tuple) and any(isinstance(x, (int)) for x in shape)):
			return np.full(shape, value)
		raise ValueError("from_shape(shape,value): shape must be an int or a tuple of ints")

	@staticmethod
	def random(shape):
		if isinstance(shape, int) or (isinstance(shape, tuple) and any(isinstance(x, (int)) for x in shape)):
			return np.random.rand(shape[0],shape[1])
		raise ValueError("random(shape): shape must be an int or a tuple of ints")

	@staticmethod
	def identity(n):
		if isinstance(n, int):
			return np.identity(n)
		raise ValueError("identity(n): n must be an int")

