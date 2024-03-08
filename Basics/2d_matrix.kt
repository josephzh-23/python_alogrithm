package Util

import java.util.*


fun main() {


    var arr = arrayOf(intArrayOf(1, 2, 3), intArrayOf(4, 5, 6), intArrayOf(7, 8, 9))
    for (row in arr) {
        println(row.contentToString())
    }

    // used to loop throught the matrix here
    for (i in 1 until arr.size) {
        for (j in 1 until arr[i].size) {
            if (arr[i][j] == 0) {
                // of that column
                arr[0][j] = 0
                // of that row
                arr[i][0] = 0
            }
        }
    }

    /*
    Main pts
    1. Create a dp array of size [n][k+1], a 2d array, size of input is 1
    initially everything in the row will be filled with -1 as said
     */
    var h = 4
    var s= 7
    val dp2 = Array(h) { IntArray(s + 1) }
    //init all array with -1
    for (row in dp2) Arrays.fill(row, -1)

    // empty array up here without initializing anything here
    // Will create  a 4* 3 matrix as said
    var (m, n) = Pair(4, 5)
    val visited = Array(m) {IntArray(n)}

    var k = 4
    val dp = Array(n) { IntArray(k + 1) }
    //init an arr of 2d of 0s
    var count = Array(4) {IntArray(4){0} }

    // How to make a 2d matrix for seen
    var seen: Array<BooleanArray?>

    Array(arr.size) { BooleanArray(arr[0].size) }
    // ArrayOf      IntArray for declaring the function the actual type as
    // explained
    // Template to solving the 2d problem as in kotlin
//    val m = grid.size.kt
//    val n = grid[0].size.kt
//    val seen = Array(m) { IntArray(n) }
}
// Array<IntArray> this would be the 2d matrix as mentioned before

