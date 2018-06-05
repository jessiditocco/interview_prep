def diagonal_difference(matrix, num):

    diagonal1 = 0
    diagonal2 = 0

    for i in range(num):
        diagonal1 += matrix[i][i]
        diagonal2 += matrix[i][(num - 1) - i]
   
    return abs(diagonal1 - diagonal2)




print diagonal_difference([
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
    ], 3)





    # diagonal1 = matrix[0][0] + matrix[1][1] + matrix[2][2]
    # diagonal2 = matrix[0][2] + matrix[1][1] + matrix[2][0]


# #!/bin/python

# import math
# import os
# import random
# import re
# import sys

# # Complete the diagonalDifference function below.
# def diagonalDifference(a):
#     len_a = len(a)
    
#     sum_d1 = 0
#     sum_d2 = 0
    
#     for i in range(len_a):
#         sum_d1 += a[i][i]
#         sum_d2 += a[i][(len_a - 1) - i]
    
#     return abs(sum_d1 - sum_d2)


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(raw_input())

#     a = []

#     for _ in xrange(n):
#         a.append(map(int, raw_input().rstrip().split()))

#     result = diagonalDifference(a)

#     fptr.write(str(result) + '\n')

#     fptr.close()
