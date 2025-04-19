package sorting


// You can use the original first and figure out what it would look like
/*
1  4  7  11  15
2  5  8  12  19
3  6  9  16  22     if tar = 20, then move down

2 conditions
1. target > pivot       r++ (move down a row)
2. target < pivot       c-- (move back a column)
3. And if not found then eventually the text
 */
fun searchMatrix2(matrix: Array<IntArray>, target: Int): Boolean {
    var r = 0
    var c = matrix[0].size - 1
    while (r < matrix.size && c >= 0) {
        if (matrix[r][c] == target) return true else if (matrix[r][c] < target) r++ else c--
    }
    return false
}