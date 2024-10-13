'''

Using the brick walls here the problem gets more interesting


Minimize the bricks crossed here

Using the count dictionary
the key is the index and the value : frequency of the edge that has been crossed here

[3, 5, 1, 1]
{3: 1, 8: 1 }

after 3rd brick 8 + 1 = 9, but we dont count this edge here

And then # 2 here:

1. Second row here, [2, 3, 3, 2]
{3: 1, 8: 1, 2: 1, 5: 1})

2. Third row is then [5, 5] and then becomes

cnt becomes {3: 1, 8: 1, 2: 1, 5: 2})


Now eventually we have

(cnt becomes {3: 1, 8: 3, 2: 2, 5: 2, 4: 2, 1: 2, 7: 1})


And we can see at position 8 we have the most data here
'''
from collections import Counter, defaultdict
from typing import List

wall = [
    [3, 5, 1, 1],
    [2, 3, 3, 2],
    [5, 5],
    [4, 4, 2],
    [1, 3, 3, 3],
    [1, 1, 6, 1, 1]
]


def leastBricks( wall: List[List[int]]) -> int:
    # Create a dictionary to count the frequency of each edge's position (except for the last edge of each row)
    edge_count = defaultdict(int)

    # Iterate over each row in the wall
    for row in wall:
        width = 0  # Initialize width to track the current position of edges

        # Iterate over each brick in the row, except the last brick
        for brick in row[:-1]:
            width += brick  # Increase the width by the current brick's length to find the next edge
            edge_count[width] += 1  # Increment the count of the edge at the corresponding width

    # If there are no edges counted, return the number of rows (since a vertical line would cross all rows)
    if not edge_count:
        return len(wall)
    print(edge_count)
    # Find the maximum occurrence of a common edge and subtract it from the total rows.
    # This gives the minimum number of rows crossed by a vertical line.
    return len(wall) - max(edge_count.values())

leastBricks(wall)