package tricks

import java.util.*

fun main() {
    var maxHeap: Queue<Int> = PriorityQueue { a: Int, b: Int -> b - a }
    var minHeap: Queue<Int> = PriorityQueue()
}
