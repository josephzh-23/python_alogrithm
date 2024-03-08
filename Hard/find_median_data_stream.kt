package Hard

import java.util.*


/*
TC:  O( 5* logn) + O(1) == Olog(n)
Heap insertion/deletion  takes O(logn) time
Median takes O(1) time here
 */
/*
If size even the
2.  the median can be derived from the tops of both heaps
3. Otherwise, the top of the max-heap lo holds the legitimate median.


 */
internal class MedianFinder
/** initialize your data structure here.  */
{
    var maxHeap: Queue<Int> = PriorityQueue { a: Int, b: Int -> b - a }
    var minHeap: Queue<Int> = PriorityQueue()
    var size = 0
    fun addNum(num: Int) {
        size++
        // Add element onto the correct heap
        if (maxHeap.isEmpty() || num <= maxHeap.peek()) {
            maxHeap.add(num)
        } else {
            minHeap.add(num)
        }

        // The median can be derived from the top of
        // both heaps

        // The max heap lo allowed to store 1 more elem than
        // min heap hi
        if (minHeap.size + 1 < maxHeap.size) {
            val element = maxHeap.poll()
            minHeap.add(element)
        } else if (maxHeap.size < minHeap.size) {
            val element = minHeap.poll()
            maxHeap.add(element)
        }
    }

    fun findMedian(): Double {
        //Odd size
        return if (size % 2 != 0) maxHeap.peek().toDouble() else (maxHeap.peek() + minHeap.peek()) / 2.0
        //Even size
    }
}

