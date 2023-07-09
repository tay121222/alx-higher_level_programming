#!/usr/bin/python3
"""Contains function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(element, list) for element in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(element, list) for element in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if any(not isinstance(element, (int, float))
            for element in m_a
            for element in element):
        raise TypeError("m_a should contain only integers or floats")

    if any(not isinstance(element, (int, float))
            for element in m_b
            for element in element):
        raise TypeError("m_b should contain only integers or floats")

    if len(set(len(element) for element in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")

    if len(set(len(element) for element in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b) or len(m_b[0]) != len(m_a):
        raise ValueError("m_a and m_b can't be multiplied")

    r1 = []
    i1 = 0

    for a in m_a:
        r2 = []
        i2 = 0
        num = 0
        while (i2 < len(m_b[0])):
            num += a[i1] * m_b[i1][i2]
            if i1 == len(m_b) - 1:
                i1 = 0
                i2 += 1
                r2.append(num)
                num = 0
            else:
                i1 += 1
        r1.append(r2)

    return r1
