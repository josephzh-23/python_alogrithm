package Util

import java.util.*

fun main() {

    // The below means that what we add to it
    //a[2] - b[2]   means we are comparing by 2nd element in array
    val minHeap = PriorityQueue { a: IntArray, b: IntArray -> a[2] - b[2] }
    minHeap.add(intArrayOf(0, 0, 0))


    val pq2 = PriorityQueue<Int>()

    pq2.add(1)
    pq2.add(2)
    pq2.add(3)
    pq2.run{
        println(poll())
    }
}


