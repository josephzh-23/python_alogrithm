package Array

fun main() {
    var arr = arrayOf(intArrayOf(1, 2, 3),
    intArrayOf(4, 5, 6),
    intArrayOf(7, 8, 9)
    )

    rotate(arr)
}
fun rotate(m: Array<IntArray>): Unit {
    //1 2 3
    // [0][0]  [0][1]   [0][2]
    // [2][0]  [2][1]  [2][2]

    // 7 4  1

    //  [2][0]   [2][1]    [2][2]
    // [0][0]   [0][1]    [0][2]
    for (i in 0 until m.size) {
        var k = m[i].size-1
        for (j in 0 until m[i].size) {

//            if (matrix[i][j] == 0) {
//                matrix[0][j] = 0
//                matrix[i][0] = 0
//            }
            // [0][0]  [2][0]
            m[i][j] = m[k][j]
            k--
        }
    }
}