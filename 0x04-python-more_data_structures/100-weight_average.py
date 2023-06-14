#!/usr/bin/python3
def weight_average(my_list=[]):
    result = sum(map(lambda x: x[0] * x[1], my_list))
    result /= sum(map(lambda x: x[1], my_list))
    return result
