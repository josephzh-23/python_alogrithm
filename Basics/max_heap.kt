package Util

import java.util.*


object maxheap {
    @JvmStatic
    fun main(args: Array<String>) {
        val k = 4
        val nums = intArrayOf(1, 2, 3, 4)

        // WHat's the actual max heap
        val maxHeapActual: Queue<Int> = PriorityQueue { a: Int, b: Int -> b - a }


        val count: MutableMap<Int?, Int?> = HashMap<Int?, Int?>()
        for (n in nums) {
            count[n] = count.getOrDefault(n, 0)!! + 1
        }
        printDictionary((count as HashMap<*, *>))

    }
}