'''

WHat we are creating here


(i + j, j, v)

(Contain the diagonal index, column index, the value)




For i = 0, row = [1, 2, 3]:

For example we belong to [1, 2, 3]

For example, 1 belongs to diagonal = 0
2 belongs to diagonal 1

    (1, 1, 2)

    For j = 0, v = 1: Compute diagonal index i + j = 0, append (0, 0, 1) to arr.
    For j = 1, v = 2: Compute diagonal index i + j = 1, append (1, 1, 2) to arr.
    For j = 2, v = 3: Compute diagonal index i + j = 2, append (2, 2, 3) to arr.

'''
from typing import List



'''

The tc is O(n* logn)
'''
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # Initialize an empty list to store the values along with their diagonal indices
        diagonal_elements = []

        # Iterate through the matrix rows
        for row_index, row in enumerate(matrix):
            # Iterate through the elements in the current row
            for column_index, value in enumerate(row):
                # The sum of row and column indices gives the diagonal index.
                # Append a tuple containing the diagonal index, column index and the value
                diagonal_elements.append((row_index + column_index, column_index, value))

        # Sort the list of tuples based on diagonal index, then by column index (as secondary)
        # This will order the elements first by diagonal, then from top-right to bottom-left
        # within the same diagonal line.
        diagonal_elements.sort()

        # Extract the values from the sorted list of tuples and return them in the correct order
        return [element[2] for element in diagonal_elements]