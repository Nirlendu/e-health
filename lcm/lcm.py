# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

def gcd(a, b):
    """
    Greatest Common Divisor - Euclid's Algorithm.
    Please refer - https://www.wikpedia.com/en/Euclidean_algorithm
    """
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    Lowest Common Multiple.
    Usinf the standard formula - a * b = GCD(a,b) * LCM(a,b)
    """
    return a * b // gcd(a, b)


def calculate_lcm(arr):
    # Initialzing the arr_lcm as first element of the list
    arr_lcm = arr[0]
    # Parsing the list from the second element, as the first element is already considered
    for each_element in arr[1:]:
        # Following the logic lcm(a, b, c) = lcm (a, lcm(b, c))
        arr_lcm = lcm(each_element, arr_lcm)
    return arr_lcm