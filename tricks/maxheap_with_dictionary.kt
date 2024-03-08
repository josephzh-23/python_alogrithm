package tricks

import java.util.*

fun main() {
    var nums = intArrayOf(1, 2, 3, 4)
    val count: MutableMap<Int?, Int?> = HashMap<Int?, Int?>()
    for (n in nums) {
        count[n] = count.getOrDefault(n, 0)!! + 1
    }
    // init heap 'the less frequent element first'
    val maxHeap2: Queue<Int> = PriorityQueue { n1: Int?, n2: Int? -> count[n1]!! - count[n2]!! }
    for (n in count.keys) {
        maxHeap2.add(n)
        //            if (heap.size() > k) heap.poll();
    }
    println(maxHeap2.poll())
}