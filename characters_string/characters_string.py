# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

from collections import OrderedDict

def common_elements(first_arr, second_arr):
	"""
	Returns a list of common elements found in both lists
	"""
	return list(set(first_arr)-set(second_arr))

def first_arr_unique_elements(first_arr, second_arr):
	"""
	Returns a list with unique elements in first list only -- Complexity -- O(N*N)
	"""
	# List of unique elements in first list
	first_arr_unique_elements = list(OrderedDict.fromkeys(first_arr))
	# List of unique elements in second list
	second_arr_unique_elements = list(OrderedDict.fromkeys(second_arr))
	# List of common elements in both lists
	common_elements_list = common_elements(first_arr_unique_elements, second_arr_unique_elements)
	# Removing each common element from first list
	for each_element in common_elements_list:
		first_arr_unique_elements.remove(each_element)
	return first_arr_unique_elements