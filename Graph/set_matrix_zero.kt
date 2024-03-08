package Graph
// set all the matrix zeros here

fun main() {
    var arr = arrayOf(intArrayOf(0, 1, 2, 0),
    intArrayOf(3, 4, 5, 2),
    intArrayOf(1, 3, 1, 5))
    setZeroes(arr)
}
fun setZeroes(matrix: Array<IntArray>) {

    // This checks if there is any 0 in the first column
    var firstCol = false
    // This checks if there is any 1 in the first row
    var firstRow = false
    // Check for Anything in 1st col of every row
    for (i in matrix.indices) {
        // [1][0]      [2][0]
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

    // Check for every cell now after 1st row and 1st col
    // if a cell is 0, then entire row and column becomes 0
    for (i in 1 until matrix.size) {
        for (j in 1 until matrix[i].size) {
            if (matrix[i][j] == 0) {
                // of that column
                matrix[0][j] = 0
                // of that row
                matrix[i][0] = 0
            }
        }
    }

    // This takes care case if a zero on the last column first row
    for (i in 1 until matrix.size) {
        for (j in 1 until matrix[i].size) {
            // if m[5][0] == 0
            // if m[5][0] == 0 and then m[5][1] = 0
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0
            }
        }
    }
    //Basically here after the scan you can check for first column
    // first row
    if (firstCol) {
        for (i in matrix.indices) {
            matrix[i][0] = 0
        }
    }
    if (firstRow) {
        for (j in matrix[0].indices) {
            matrix[0][j] = 0
        }
    }
}