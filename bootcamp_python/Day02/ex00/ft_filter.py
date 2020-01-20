def ft_filter(function_to_apply, list_of_inputs):
	if not list_of_inputs:
		raise ValueError("ft_filter require 2 args")

	result = []
	for item in list_of_inputs:
		if function_to_apply(item) == True:
			result.append(item)
	return result