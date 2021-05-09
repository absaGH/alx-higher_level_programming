#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    Delkeys = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            Delkeys.append(key)
    for key in Delkeys:
        del a_dictionary[key]
    return a_dictionary
