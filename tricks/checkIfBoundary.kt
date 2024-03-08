package tricks

fun checkIfBoundary(a: Array<IntArray>, m: Int,
                   n: Int){

    var numElemOnEdge = 0
    var sum: Long = 0
    for (i in 0 until m) {
        for (j in 0 until n) {
            // Firt row
            if((i == 0) ||(i == m - 1)|| (j == 0)
                    ||(j == n - 1)){
                numElemOnEdge++
            }
        }
    }
    println(numElemOnEdge)
}

/* Driver code */
fun main(args: Array<String>) {
    val a = arrayOf(intArrayOf(1, 2, 3, 4), intArrayOf(5, 6, 7, 8),
            intArrayOf(1, 2, 3, 4), intArrayOf(5, 6, 7, 8))
    val sum = checkIfBoundary(a, 4, 4)


}