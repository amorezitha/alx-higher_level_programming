#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = dir(a_dictionary)
    for i in a_dictionary:
        new_dir[i] *= 2
        return new_dir
