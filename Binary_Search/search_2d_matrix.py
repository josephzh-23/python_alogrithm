from typing import List

"""

1. 2 while loops, 1 for searching the mid row and the other for 
searching for value 

2.     row = (top + bot) // 2
and then do the while loop practice 


Some properties 
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

"""


#  log (n) + log (m)
def searchMatrix( matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])

    top, bot = 0, ROWS - 1

    # this gives middle row
    while top <= bot:
        row = (top + bot) // 2

        # compare this with the last value on that row
        # print('this here is ', matrix[row][-1])
        if target > matrix[row][-1]:
            top = row + 1


        # compare with the first value on that row
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break

    # In this case value not found
    if not (top <= bot):
        return False
    row = (top + bot) // 2
    l, r = 0, COLS - 1

    # just typical bin Search on that row
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False


matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]
target = 23
print('teh value found is', searchMatrix(matrix, target))