#!/usr/bin/python3
def print_list_integer(my_list=[]):
    print(*map(lambda x: '{}'.format(x), my_list), sep='\n')
