from typing import List


# Get the maximum area in a histogram given its heights
def leetcode84(heights):
    # this acts as a gauard rail
    stack = [-1]

    maxarea = 0
    for i in range(len(heights)):

        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            popped = stack.pop()
            maxarea = max(maxarea, heights[popped] * (i - stack[-1] - 1))
        stack.append(i)

    while stack[-1] != -1:
        maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
    return maxarea


'''We can compute the maximum width of a rectangle that ends at a given coordinate in constant time. We do this by 
keeping track of the number of consecutive ones each square in each row. As we iterate over each row we update the 
maximum possible width at that point. This is done using row[i] = row[i - 1] + 1 if row[i] == '1'. 

like we said a maximal rectangle here: 

'''



def maximalRectangle(matrix: List[List[str]]) -> int:
    if not matrix:
        return 0

    maxarea = 0
    dp = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # update the state of this row's histogram using the last row's histogram
            # by keeping track of the number of consecutive ones

            dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0

        # update maxarea with the maximum area from this row's histogram
        maxarea = max(maxarea, leetcode84(dp))

    print('max area is', maxarea)
    return maxarea


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
maximalRectangle(matrix)
