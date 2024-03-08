package Basics

import java.util.ArrayList

fun main() {

    val prerequisites = arrayOf(
        charArrayOf('a', 'b'),
        charArrayOf('b', 'c'),
        charArrayOf('d', 'e')
    )
    val map = mutableMapOf<Char, ArrayList<Char>>()

    val m = prerequisites.size
    for (i in 0 until m) {
        val start = prerequisites[i][0]
        val end = prerequisites[i][1]
        map.putIfAbsent(start, ArrayList())
        map[start]?.add(end)
    }

    // Will allow you to loop through that particular number here
    val node = 'a'
    for(num in map[node]!!){
        print(num)
    }
}