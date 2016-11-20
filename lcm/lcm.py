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
    arr_lcm = arr[0]
    for each_element in arr[1:]:
        arr_lcm = lcm(each_element, arr_lcm)
    return arr_lcm