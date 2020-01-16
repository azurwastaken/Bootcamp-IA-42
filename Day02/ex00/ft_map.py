def ft_map(function, iterable):
	result = []
	if not iterable:
		raise ValueError("ft_map should have 2 args")
	if not (hasattr(iterable, "__iter__") or isinstance(iterable, str)):
		raise TypeError(f"'{type(iterable)}' is not iterable")
	for item in iterable:
		result.append(function(item))
	return iterable
