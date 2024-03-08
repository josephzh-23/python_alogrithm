package tricks


fun main() {
    var arr = intArrayOf(1, 2, 3, 4)
    checkConsecutiveLoop(arr, 5)
}

fun checkConsecutiveLoop(arr: IntArray, sum: Int) {
    var n = arr.size
    for (i in 0 until n) {
        for (j in i + 1 until n) {
            if (arr[i] + arr[j] == sum) {
                println("$i and $j")
            }
        }
    }
}