#!/usr/bin/python3
def no_c(my_string):
    # Filter out 'c' and 'C' using a list comprehension or generator
    new_string = "".join([
    char for char in my_string if char not in ('c', 'C') ])
    return new_string
