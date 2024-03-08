package sorting


/*

 1   3   5   7
10  11  16  20
23  30  34  50

midpoint = 5        5 would be the mid point of 11
matrix[1][1]    ==11
 */
    fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
        if (matrix.size == 0) return false
        val n = matrix.size
        val column = matrix[0].size

        // first elem in entire matrix
        var left = 0
        // The last element on the last column
        var right = n * column - 1
        while (left <= right) {
            val mid = left + (right - left) / 2

            // 11 would give you 5 like said
            if (matrix[mid / column][mid % column] == target) {
                return true
            }
            if (matrix[mid / column][mid % column] < target) {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return false
    }