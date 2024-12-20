from typing import List


def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    m, n = len(matrix), len(matrix[0])
    for i in range(1, m):
        for j in range(1, n):
            if i == j:
                if matrix[i - 1][j - 1] != matrix[i][j]:
                    return False

    return True
