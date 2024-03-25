#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
         returns a list of lists of
         integers representing
          the Pascal’s triangle of n
         Returns an empty list if n <= 0
    """
    pascal_list = []
    for i in range(n):
        number_list = []
        for j in range(i+1):
            if j == 0 or j == i:
                number_list.append(1)
            else:
                number_list.append(pascal_list[i-1][j] + pascal_list[i-1][j-1])
        pascal_list.append(number_list)
    return pascal_list
