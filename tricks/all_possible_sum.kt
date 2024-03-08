package tricks

fun main() {
    var arr = intArrayOf(1, 2, 3, 4)
    checkConsecutiveSum(arr, 5)
}

fun checkConsecutiveSum(arr: IntArray, sum: Int) {
    var n = arr.size
    // Will start from [0, 1] [0, 2] [0, 3]
    // [1, 2]   [1, 3]      [2, 3]
    for (i in 0 until n) {
        for (j in i + 1 until n) {
//            if (arr[i] + arr[j] == sum) {
                println("$i and $j")
//            }
        }
    }
}