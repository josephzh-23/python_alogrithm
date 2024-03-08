package Util

fun main() {
    var memo = HashMap<Pair<Int, Int>, Int>()

    memo.put(Pair(1,1), 2)
    println(memo.contains(Pair(0,0)))
    println(memo.contains(Pair(1,1 )))
}