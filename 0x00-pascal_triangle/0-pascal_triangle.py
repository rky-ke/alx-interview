#!/usr/bin/python3
# n = int(input("Enter number of rows:"))
def pascal_triangle(n):
    """
    Returns a Pascal triangle
    """
    pascal_list = []
    for i in range(n):
        number_list = []
        for j in range(i+1):
            if j==0 or j== i:
                number_list.append(1)
            else:
                number_list.append(pascal_list[i-1][j] + pascal_list[i-1][j-1])
        pascal_list.append(number_list)
    # for i in range(n):
    #     for j in range(n-i-1):
    #         print(format(" ", "<2"), end="")
    #     for j in range(i+1):
    #         print(format(pascal_list[i][j], "<3"), end=" ")
    #     print()
    return pascal_list