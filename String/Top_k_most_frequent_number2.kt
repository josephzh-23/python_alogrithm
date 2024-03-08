package String

import java.util.*


fun topKFrequent(nums: IntArray, k: Int): IntArray? {
    // O(1) time
    if (k == nums.size) {
        return nums
    }

    // 1. build hash map : character and how often it appears
    // O(N) time
    val count: MutableMap<Int?, Int?> = HashMap()
    for (n in nums) {
        count[n] = count.getOrDefault(n, 0)!! + 1
    }

    // init heap 'the less frequent element first'
    // Still a min heap though
    val minHeap: Queue<Int> = PriorityQueue { n1: Int?, n2: Int? -> count[n1]!! - count[n2]!! }

    // 2. keep k top frequent elements in the heap
    // O(N log k) < O(N log N) time
    for (n in count.keys) {
        minHeap.add(n)
        if (minHeap.size > k) minHeap.poll()
    }

    // 3. build an output array
    // O(k log k) time
    val top = IntArray(k)
    for (i in k - 1 downTo 0) {
        top[i] = minHeap.poll()
    }
    top.forEach{
        println(it)
    }
    return top
}
fun main(){
    var nums = intArrayOf(4, 3, 3, 3, 3, 2, 1, 2)
    topKFrequent(nums, 2)

}