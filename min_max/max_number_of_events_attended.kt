package Array.Min_max

import java.util.*


fun main() {
    var arr = arrayOf(intArrayOf(1, 2), intArrayOf(2, 3), intArrayOf(3, 4))

    maxEvents(arr)
}

fun maxEvents(es: Array<IntArray>): Int {


    // Storing the end time
    val pq: Queue<Int> = PriorityQueue()
    Arrays.sort<IntArray>(es) { a, b-> a[0] - b[0] }
    var i = 0
    var res = 0
    val n = es.size


    // This will come here dependeing on the size of the input
    for (d in 0..es.size) {


        // Here the es[i][0] is the starting day here
        while (i < n && es[i][0] == d) {
            pq.offer(es[i++][1])
        }
        println(pq.peek()?:0)

        // [1, 2], [1, 2] , [2, 2] will not work anymore
        // day here would be 2 and [2, 2] would be sth else


        // Check if the end less than the day
        while (pq.size > 0 && pq.peek() < d) {
            pq.poll()
        }



        // Here the pq has event > d
        println(pq.size)
        if (!pq.isEmpty()) {
            pq.poll()
            res++
        }

        if (pq.isEmpty() && i >= n) {
            break
        }
    }
    return res
}