# how to assign a list to a matrix, work with matrix basic
mat = ['110', '110', '001']
def ans(arr):
    # matrix = [[0]*len(mat)]*len(mat)
    # print(matrix)
    arr = []
    print(arr)

    rowNum = 0
    for row in mat:
        print(row)

        col = []
        for column in range(len(row)):
            col.append(int(row[column]))
        arr.append(col)
        rowNum+=1
    print(arr)
ans(mat)