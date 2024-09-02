'''


Do we really need to store all the heights in the stack here?

Simply put, while traversing from right to left, the current building will
 only have an ocean view if it is the tallest building seen so far.
'''
from typing import List


def findBuildings(self, heights: List[int]) -> List[int]:
    n = len(heights)
    answer = []
    max_height = -1
    # we need to go from the back here
    for current in reversed(range(n)):
        # If there is no building higher (or equal) than the current one to its right,
        # push it in the answer array.
        if max_height < heights[current]:
            answer.append(current)

            # Update max building till now.
            max_height = heights[current]

    answer.reverse()
    return answer