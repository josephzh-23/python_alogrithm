package Array


// Kind of like 2 sum problem
fun main() {

    var arr = intArrayOf(1, 2, 3, 4, 3)
    var k = 6
    numOfWays(arr, k)
}

fun numOfWays(arr:IntArray, k: Int){

    var map = mutableMapOf<Int, Int>()
    var count = 0
    for (i in arr) {
        val diff = k-i
        if (map.contains(diff)) {
            count += map[diff]!!
        }
        map.putIfAbsent(i, 0)
        map[i] = map[i]!! + 1
    }
    println(count)
}