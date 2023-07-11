#!/usr/bin/python3
"""Module that saves args to json file"""


from sys import argv
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

argv = argv[1:]
filename = 'add_item.json'

save([], filename)
my_list: list = load(filename)
my_list.extend(argv)
save(my_list, filename)
