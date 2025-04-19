'''


Canvas painted white here

presence of a square with a k side length here
- All cells are colored

M and n # of rows and columsn here

paints[i][0]
paints[i][1]    represnts the cell coordinate to be painted black during the ith minute here

ps[0][0] = 1
ps[0][1] = 2

If the inputs are [[1, 2], [2, 3], [2, 1], [1, 3], [2, 2], [1, 1]]

And then you have
'''
from Matrix.range_sum_query_2d_immutable import NumMatrix

'''
Anywhere we have the inputs coordinates x and y we can then try to make it a 1 to start 


'''
def buildPaint(inputs, n, m, k):
    matrix = [[0] * m for j in range(n)]
    print(matrix)
    time = 0
    for x, y in inputs:
        '''
        Build a matrix 
        '''
        matrix[x-1][y-1] =1
        s = NumMatrix(matrix)
        numOfBlacks = s.sumRegion(0, 0, n-1,  m -1 )
        time+=1
        if (numOfBlacks == k*k):
            print("we have reached our time" , time)
    # print(matrix)
inputs =  [[1, 2], [2, 3], [2, 1], [1, 3], [2, 2], [1, 1]]
buildPaint(inputs, 2, 3, 2)