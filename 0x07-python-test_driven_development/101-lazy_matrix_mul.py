#!/usr/bin/python3
"""Module for matrix_mul function"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """multiplies two matrices

    Args:
        m_a (list): the first operand
        m_b (list): the second operand

    Returns: the result
    """
    return numpy.dot(m_a, m_b)
