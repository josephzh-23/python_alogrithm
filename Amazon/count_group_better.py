matrix = ["1100","1110","0110","0001"]

# convert the above to [[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]


# same as using number of connected islands example as said
# you can do a dfs on this
def countGroups(related):
    # convert the above to array
    result = []
    count = 0
    for char in related:
        print(char)
        result.append([int(x) for x in char])
    print(result)
    length = len(result)

    rowlen = len(result)
    collen = len(result[0])

    count = 0

    for r in range(0, rowlen):
        for c in range(0, collen):
            if result[r][c] == 1:
                find(r, c, result)
                count +=1

    print(count)

def find(r, c, grid):
    if r< 0 or r>= len(grid) or c< 0 or c>= len(grid[0]) or grid[r][c] ==0:
        return

    if grid[r][c] == 1:
        grid[r][c] = 0
        find(r - 1, c, grid)
        find(r + 1, c, grid)
        find(r, c + 1, grid)
        find(r, c - 1, grid)
# what's the length here?
def dfs(idx, length, matrix):
    print('value is', matrix[idx][idx])
    if matrix[idx][idx] == 0:
        return
    for i in range(length):
        if matrix[idx][i] == 1:
            matrix[idx][i] = 0
            dfs(i, length, matrix)


countGroups(matrix)

