
'''
Done using binary search here

The idea is very simple if you have

'''

def kthSmallestElement(matrix, k):

    n = len(matrix)
    min, max = matrix[0][0] , matrix[n-1][n-1]

    # your binary search here
    while( min != max):
        mid = min + (max - min) /2
        count = countOrLessOrEqual(matrix, mid)

        if (count < k):
            min = mid + 1
        else:
            max = mid

'''
Cause the column is the issue here so deal with that first 
[1, 5, 9
10 11 13
12 13 15]   and then we have the code where
 
 mid = 8 first      start with matrix[0][2]
Compare 9 with 8, bigger, so dec col and then 

And then matrix[0][1]   ->  yes so 
then matrix[
'''

def countOrLessOrEqual(matrix, mid):
    count = 0
    col = len(matrix) - 1;  row = 0

    while row < len(matrix) and col >=0:
        if matrix[row][col] <= mid:
            count += col +1
            row+=1
        else:
            col-=1








