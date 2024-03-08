package Basics

import java.util.*

// Priority queue also work with lists in here
fun main() {
    var pq = PriorityQueue<List<Int>>{a, b-> a[0]- b[0]}
    pq.add(listOf(7, 2, 3, 4))
    pq.add(listOf(5, 2, 3, 4))
    pq.add(listOf(3, 2, 3, 4))
    println(pq.poll())
}

// Here will build a prioirty queue and a list right here
