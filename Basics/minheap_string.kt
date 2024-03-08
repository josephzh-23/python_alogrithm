package Util

import java.util.*

fun main() {

    val pq = PriorityQueue<String>()
    val pq2 = PriorityQueue<Int>()

    pq2.add(1)
    pq2.add(2)
    pq2.add(3)
    pq2.run{
        println(poll())
    }
    pq.add("xeno")
    pq.add("kuroko")
    pq.add("kagami")
    pq.add("Aomie")
    pq.run{
        println(poll())
    }
}