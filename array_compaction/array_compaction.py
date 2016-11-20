# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############


def array_compaction(arr):
	"""
	Since python lists are immutable, we have to create a new list instead of modifying the existing one
	"""
	compact_array = []
	# Index always points to the last element of the compact_array. Since compact_array is [] initially, index in None
	index = None
	for i in arr:
		# Initialzing the compact_array
		if compact_array == []:
			compact_array.append(i)
			index = 0
			continue
		# Last element of the compact_array has the current element, so the current element is repeated. Skip
		elif compact_array[index] == i:
			continue
		else:
		# Last element of the compact_array doesn't has the current element, so the current element is appended.
			compact_array.append(i)
			index += 1
	return compact_array