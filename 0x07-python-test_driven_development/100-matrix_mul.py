#!/usr/bin/python3
"""Module for matrix_mul function"""


def matrix_mul(m_a, m_b):
    """multiplies two matrices

    Args:
        m_a (list): the first operand
        m_b (list): the second operand

    Returns: the result
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if not all(map(lambda i: isinstance(i, list), m_a)):
        raise TypeError('m_a must be a list of lists')
    if not all(map(lambda i: isinstance(i, list), m_b)):
        raise TypeError('m_b must be a list of lists')
    if m_a == [] or m_a == [[]]:
        raise ValueError('m_a can\'t be empty')
    if m_b == [] or m_b == [[]]:
        raise ValueError('m_b can\'t be empty')
    if not all(all(isinstance(n, (int, float)) for n in row) for row in m_a):
        raise TypeError('m_a should contain only integers or floats')
    if not all(all(isinstance(n, (int, float)) for n in row) for row in m_b):
        raise TypeError('m_b should contain only integers or floats')
    if len(set(map(len, m_a))) != 1:
        raise TypeError('each row of m_a must be of the same size')
    if len(set(map(len, m_b))) != 1:
        raise TypeError('each row of m_b must be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')
    rows, cols = len(m_a), len(m_b[0])
    matrix = []
    for row in range(rows):
        matrix.append([])
        for col in range(cols):
            sum = 0
            for i in range(len(m_a[0])):
                sum += m_a[row][i] * m_b[i][col]
            matrix[row].append(sum)
    return matrix
