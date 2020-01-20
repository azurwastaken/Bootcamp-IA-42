def ft_reduce(function_to_apply, list_of_inputs):
	if not list_of_inputs:
		raise ValueError("ft_filter require 2 args")
	result = list_of_inputs[0]
	for item in list_of_inputs[1:]:
		result = function_to_apply(result, item)
	return result