package Graph


// set all the matrix zeros here

fun main() {
    var arr = arrayOf(intArrayOf(0, 1, 2, 0),
            intArrayOf(3, 4, 5, 2),
            intArrayOf(1, 3, 1, 5))

    setZeroesbf(arr)
}
fun setZeroesbf(matrix: Array<IntArray>) {
    var r = matrix.size
    var c = matrix[0].size
    val g = Array(matrix.size) { IntArray(matrix[0].size) }
    val rows: MutableSet<Int> = HashSet()
    val cols: MutableSet<Int> = HashSet()
    for (i in 0 until r) {
        for (j in 0 until c) {
            if(matrix[i][j] ==0) {
                rows.add(i)
                cols.add(j)
            }
        }
    }

    // Iterate over the array once again and using the rows and cols sets, update the elements.
    for (i in 0 until r) {
        for (j in 0 until c) {
            // m[0][1] if rows.contains(0)
            if (rows.contains(i) || cols.contains(j)) {
                matrix[i][j] = 0
            }
        }
    }
}