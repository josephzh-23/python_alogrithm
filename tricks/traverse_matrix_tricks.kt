fun setZeroes(matrix: Array<IntArray>) {

    // This checks if there is any 0 in the first column
    var firstCol = false
    // This checks if there is any 1 in the first row
    var firstRow = false
    // Check for Anything in 1st col of every row
    // [1][0]      [2][0]
    for (i in matrix.indices) {
        if (matrix[i][0] == 0) {
            firstCol = true
            break
        }
    }
    //Check for anything in 1st row of every column
    for (i in matrix[0].indices) {
        // [0][1]   [0][2]
        if (matrix[0][i] == 0) {
            firstRow = true
            break
        }
    }
}
