package Search

fun main() {

}

/*
When the target > pivot r++
when target < pivot c--

O(R+ C)
O(1)
 */

fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
    var (r, c) = Pair(0, matrix[0].size - 1)
    while(r < matrix.size && c>=0){
        if(matrix[r][c] == target) return true
        else if (matrix[r][c] < target) r++
        else c--
    }
    return false
}