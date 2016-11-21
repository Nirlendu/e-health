# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

def rotate(arr, n):
	"""
	Right side rotation of an array by n positions
	"""
	# Storing the length to avoid recalculation
	arr_len = len(arr)
	# Adjusting the value of n to account for Right side rotations and cases where n > length of the array
	n = arr_len - (n % arr_len)
	# Splitting the array into two parts and merging them again in reverse order (Second part + First part)
	return arr[n:] + arr[:n]