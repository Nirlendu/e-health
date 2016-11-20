# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

from collections import OrderedDict


def unique_elements_non_linear(first_arr, second_arr):
	"""
	Returns a list with common elements in order of appearance in first list -- Complexity -- O(N*N)
	"""
	# List of common elements in both lists
	common_elements_list = list(set(first_arr).intersection(set(second_arr)))

	# Init the result array
	result_arr = []

	# Itirate over first array
	for each_element in first_arr:
		# If the element is present in common_elements_list, append to result_arr
		if each_element in common_elements_list:
			result_arr.append(each_element)

	return result_arr


def unique_elements_linear(first_arr, second_arr):
	"""
	Returns a list with common elements in order of appearance in first list -- Complexity -- O(N)
	"""
	reference_dict = OrderedDict()

	# Itirating over each element of first array
	for each_element in first_arr:
		# If the element is repeatation, skip
		if each_element in reference_dict:
			continue
		# If first time, then add to reference_dict and set the value to False
		else:
			reference_dict[each_element] = False

	# Itirating over each element of second array
	for each_element in second_arr:
		# If the key is present, then it is common in both arrays
		if each_element in reference_dict:
			reference_dict[each_element] = True
		# If the key is not present, then the element is not present in first array
		else:
			continue

	# Init the result array
	result_arr = []

	for key,val in reference_dict.items():
		# The keys which are present in both arrays
		if val == True:
			result_arr.append(key)

	return result_arr
