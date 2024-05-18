'''
This is prob from before here, and then
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle
defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example

In terms of this question, we have here

Result between (r1, c1) and (r2, c2) here we have the code
= (r2, c2) - ([r2, c1 -1] + [r1 -1, c2] - [r1-1, c1 -1 ]
'''
from typing import List

'''
THere is a better question here to do here 
..
'''
def prefixSum():

    def __init__(s, matrix: List[List[int]]):
        # using the range value here we have the code
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] += matrix[i][j-1]

        # a bit of a prefix sum concept here
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):

                # and the above solutions shoudl work here
                matrix[i][j] += matrix[i-1][j]

        s.matrix = matrix

    def sumRegion(s, row1, col1, row2, col2):
        total = s.matrix[row2][col2]

        # we need an outer layer of 0 aroudn the current matrix
        extra = (s.matrix[row2][col1 - 1] if col1 != 0 else 0) + \
                (s.matrix[row1 - 1][col2] if row1 != 0 else 0) - \
                (s.matrix[row1 - 1][col1 - 1] if (row1 != 0 and col1 != 0) else 0);
        # a bit of a complicated problem here
        return total - extra