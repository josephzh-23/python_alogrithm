package Array.two_dimension

fun main() {

}
// Bsically transpose and then reverse here that's it
internal class Solution {
    fun rotate(matrix: Array<IntArray>) {
        transpose(matrix)
        reverse(matrix)
    }

    fun transpose(matrix: Array<IntArray>) {
        val n = matrix.size
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                val tmp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = tmp
            }
        }
    }

    // Here we just reverse in the middle here
    fun reverse(matrix: Array<IntArray>) {
        val n = matrix.size
        for (i in 0 until n) {
            for (j in 0 until n / 2) {
                val tmp = matrix[i][j]
                matrix[i][j] = matrix[i][n - j - 1]
                matrix[i][n - j - 1] = tmp
            }
        }
    }
}