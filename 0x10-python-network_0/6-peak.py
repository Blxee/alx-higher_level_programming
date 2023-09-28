#!/usr/bin/python3
""" Module for the find_peak() function """


def find_peak(list_of_integers):
    """Determines the peak integer in a list"""
    peak = None
    for i in list_of_integers:
        if peak is None or i > peak:
            peak = i
        else:
            break
    return peak
