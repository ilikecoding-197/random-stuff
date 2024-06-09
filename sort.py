import random


def sort(arr):
	arr = list(arr)
	
	index = None
	while index != -len(arr)+1:
		new_arr = arr[:index]
		
		if index is None:
			index = -1
		else:
			index -= 1
		
		highest = max(new_arr)
		
		while new_arr[-1] != highest:
			random.shuffle(new_arr)
		
		for i in range(len(new_arr)):
			arr[i] = new_arr[i]
	
	return arr
