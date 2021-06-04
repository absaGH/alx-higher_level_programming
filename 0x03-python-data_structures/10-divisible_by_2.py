#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result_list = []
    if my_list:
        for val in my_list:
            result_list.append(False if val % 2 else True)
    return result_list
