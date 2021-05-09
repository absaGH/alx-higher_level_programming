#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def sAndr_val(val):
        return (val if val != search else replace)
    return list(map(sAndr_val, my_list))
