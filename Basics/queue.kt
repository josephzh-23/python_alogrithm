package Util

import java.util.*


// This is not thread safe as said
// O(log (n)) for add and poll method

fun main() {
    val q = LinkedList<Int>()
    q.add(4)
    q.add(5)
    q.add(6)
    val pQueue = PriorityQueue<Int>()
    pQueue.offer(10)
    pQueue.offer(20)
    pQueue.offer(15)

    // Printing the top element of PriorityQueue
    println(pQueue.peek())

    println(pQueue.poll())

    println(pQueue.peek())
}
