#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = dict(a_dictionary)
    for i, k in a_dictionary:
        new_dir[i] =k * 2
        return new_dir
