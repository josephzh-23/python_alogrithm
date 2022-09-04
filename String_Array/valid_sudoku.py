import collections
from typing import List


''' 
Visual representation here would be
The square here would be converted from row and column using

1. Row 4, column 8  -> would fall into [ 4/3, 8/3] -> [1, 2] as explained
2. We need to check the square as well 
'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)

        # there would be 9 sqaures

        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):

                # in the case it's empty here
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True