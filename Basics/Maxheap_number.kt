package Util

import java.util.*


fun main(args: Array<String>) {
    // create priority queue
    val prq = PriorityQueue(Collections.reverseOrder<Int>())

    // insert values in the queue
    prq.add(6)
    prq.add(9)
    prq.add(5)
    prq.add(64)
    prq.add(6)

    //print values
    while (!prq.isEmpty()) {
        print(prq.poll().toString() + " ")
    }

}
