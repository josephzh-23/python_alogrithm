package sorting

import Basics.printMatrix
import java.util.*


// Sort the problem here

var meet = arrayOf(
        intArrayOf(0, 30), intArrayOf(5, 10),
        intArrayOf(15, 20)
)

var meet2 = arrayOf(
        intArrayOf(7,10), intArrayOf(2, 4)
)

fun main() {
    // Sort by the first element of each array
    //
    // the interval start -> end here
    Arrays.sort(meet2) { a, b -> a[0] - b[0] }
    printMatrix(meet2)
}