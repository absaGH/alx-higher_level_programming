#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        val = 0
        num = 0
        for tpl in my_list:
            val += (tpl[0] * tpl[1])
            num += tpl[1]
        return (val / num)
    return 0
