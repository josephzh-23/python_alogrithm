package Util

import java.util.*

fun main() {

    val pq = PriorityQueue<Char>()

    pq.add('b')
    pq.add('c')
    pq.add('a')
    pq.poll()
    pq.forEach{
        println(it)
    }
}
