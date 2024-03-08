package Dynamic_programming


//https://leetcode.com/problems/range-sum-query-2d-immutable/
class NumMatrix(matrix: Array<IntArray>) {
    var r = matrix.size
    var c = matrix[0].size

    // the 2d table we were looking at earlier the prefix sum table
    // here
    // to account for the 2d situation here from before
    var matSum: Array<IntArray> = Array(r + 1) { IntArray(c + 1) }

    init {
        // Fill sum value for row 1 and col 1
        for (i in 1 until r + 1) {
            // Fill it for the column here
            for (j in 1 until c + 1) {
                // THis is the formula that we were using before
                matSum[i][j] = matSum[i - 1][j] + matSum[i][j - 1] - matSum[i - 1][j - 1] + matrix[i - 1][j - 1]

            }
        }
    }

    fun sumRegion(row1: Int, col1: Int, row2: Int, col2: Int): Int {
        // bottom right - top right - bottom left + top left
        // below is just the formula and don't ask how it works here
        val sum = matSum[row2 + 1][col2 + 1] - matSum[row1][col2 + 1] - matSum[row2 + 1][col1] + matSum[row1][col1]
        return sum
    }
}

fun main() {
    val ss = NumMatrix(arrayOf(intArrayOf(3, 0, 1, 4, 2),
            intArrayOf(5, 6, 3, 2, 1), intArrayOf(1, 2, 0, 1, 5),
            intArrayOf(4, 1, 0, 1, 7),
            intArrayOf(1, 0, 3, 0, 5)))
    //should give back the 8
    ss.sumRegion(2, 1, 4, 3)
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */