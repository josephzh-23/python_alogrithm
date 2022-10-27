from collections import deque
from typing import List


def searchMatrix( matrix: List[List[int]], tar: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])

    # row and the matrix

    top, bot = 0, ROWS-1

    while top <= bot:
        mid = (top +bot)//2

        if tar > matrix[mid][-1]:
            top = mid +1