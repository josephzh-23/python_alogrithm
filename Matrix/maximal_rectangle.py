'''

This is the problem here

If we carefully observe, we can convert each row of the given matrix into a histogram. Let’s try it out with the first row: We can consider the first and third columns to be rectangles with height 1 and the rest to be rectangles with height 0. The histogram will look like the following:
[1, 0, 1, 0, 0]

Convert into histogram

WIth 2nd row it beomces
[1, 0, 1, 0, 0]
[1, 0, 1, 1, 1]

This is like arae of the largest rectanlge in histogram here in this question.
We will consider the max one


Declare a height array of size m(where m = no. of columns of the matrix).

Now inside the loop
1. For each row:

for each row, iterate over every column, and if a cell contains 1 we will increase the value of the column index by 1 in the height array i.e.

2.  But if the cell contains 0, we will set 0 for that column index in the height array.

3.
Once every cell gets visited, we will pass the height array i.e. the histogram array to the largestRectangleArea() function and store the maximum area for the row.
'''

def maximalRectangle(histo):
    st = []
    maxA = 0
    n = len(histo)
    for i in range(n):
        while st and (i== n or histo[st[0]>=histo[i]]):
            height = histo[st.pop()]







