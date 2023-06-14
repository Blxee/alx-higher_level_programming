#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary is None:
        return max(a_dictionary.keys(), key=a_dictionary.get)
