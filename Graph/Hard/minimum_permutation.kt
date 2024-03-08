package Graph.Hard//import java.util.*
//
//
//
//fun minOperations(arr: IntArray): Int {
//    val updatedIndexes: MutableMap<Int, Int> = HashMap()
//    val heap = PriorityQueue { a: Int, b: Int -> a - b }
//    for (i in arr.indices) {
//        heap.add(arr[i])
//        updatedIndexes[arr[i]] = i
//    }
//    var curr = 0
//    var swapCount = 0
//    while (!heap.isEmpty()) {
//        val n = heap.poll()
//        if (n < arr[curr]) {
//            reverse(arr, Math.min(updatedIndexes[n]!!, curr), Math.max(updatedIndexes[n]!!, curr), updatedIndexes)
//            swapCount++
//        }
//        curr++
//    }
//    return swapCount
//}