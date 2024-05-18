'''
Solve the 1-d case here first and then keep going here

- Case 1d: 1 - 0 - 0 - 0 - 1 here

- case 2: 0 - 1 - 0 - 1 - 0 here

Arrange the data points from smallest to largest. If the number of data points is odd, the median is the middle data
point in the list. If the number of data points is even, the median is the average of the two middle data points in
the list.

Qzhou here then we can have this situation

Part 1:
The median for the rows is simply the middle element of the rows list. This works because the grid rows are already
indexed in sorted order.

and then using the code here we have a much better time to use this then the other one here

Part 2: The median for the column:
    we need to sort the cols list before finding the middle element, which serves as the median.

    trying to rush through this problem right here and then we have the following here which is not so good here


Part 3:
    create the rows x, y to build all the x and y coordinates here,

Part 3:

Finally, the function f(arr, x) calculates the sum of distances of all points in arr to point x, the median. The
minTotalDistance function returns the sum of f(rows, i) and f(cols, j), where i and j are the median row and column
indices, representing the optimal meeting point.

Calculates the sum here and then all the sum of the distances here the minimum distance here

Part 4:

1. Sum up abs(v-x ) for all values in arr: here and then we have the code

2 lists: rows and columsn here:

    We achieve this by iterating through every cell in the grid with nested loops. When we find a cell with a 1,
    we append the row index i to rows and the column index j to cols.

And then

3. Then sum up all the toal Manhattan distance from all friend's homesto the median point by callling

f(rows, i) + f(cols, j) here
Store the row and column here

Example here

1 0 0
0 1 0
0 0 1       and this is the one here and then we have, may need to sort the list here

And then using the formula given:
f(rows, i) = abs(0 - 1) + abs(1 - 1) + abs(2 - 1) = 1 + 0 + 1 = 2.
f(cols, j) = abs(0 - 1) + abs(1 - 1) + abs(2 - 1) = 1 + 0 + 1 = 2.

And eventually we land as
2 + 2 = 4 as the minimum total travel distance here

Using python sort we have

    '''
from typing import List

'''
This is part 1 here: 
Formula is abs(p2.x - p1.x) + abs(p2.y - p1.y)
And then here we can have the code a little bit better then this 
And then using the sorting here 
'''
def minDistanceToAll(grid: List[List[int]])-> int:
    # and then we have the code
    m, n = len(grid), len(grid[0])

    # these 2 are the first ones here


    rows, cols, houses = [], [], []

    #and now once you have the i and j here that's good here
    # and then here we have O (m * n) here then and then we have the code
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                houses.append([i, j])


    for j in range(n):
        for i in range(m):
            if grid[i][j] == 1:
                cols.append(j)

    # find the median first here and then we have the code
    medianRow = rows[len(rows)//2]
    medianCols = cols[len(cols)//2]

    # and now once you get these 2 would be a good starting point
    # and these r the first 2 starting ponits

    # and this is part 1 of this equation here

    # and then here the code is done here
    return sum([abs[houses[0] - medianRow] + abs(house[1] - medianCols) for house in houses])
