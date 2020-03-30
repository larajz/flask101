##################################################################
# *** DO NOT EDIT THIS FILE ***
# All the functions below take a list of numbers as an argument
##################################################################



def mean(number_list):
	size = len(number_list)

	return 0 if size == 0 else sum(number_list)/size


def median(number_list):
	number_list.sort()

	size = len(number_list)

	if size == 0: 
		median_index = "No median found because list is empty"
	else: 
		median_index = int(size / 2) + size % 2

	return median_index


def mode(number_list):
	if len(number_list) == 0:
		mode_value = "No mode found because list is empty"
	else: 
		mode_value = max(set(number_list), key=number_list.count)

	return mode_value
