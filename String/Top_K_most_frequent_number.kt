//package String
//
//import java.util.*
//
//// OC: O(klogD + DlogD)     D: count of distinct elemn in arrayi
///*
//To remove the top of the priority queue O(log d) time is required,
//so if k elements are removed then O(k log d) time is required, and
//To construct a priority queue with D elements, O(D log D) time is required.
// */
//// SC: O(d)     count of distinc elem in array
//
//// Find most frequent element here
//fun topKMostFrequentElements(nums:IntArray, k: Int):IntArray{
//
//    // {3: 2}       <number, count>
//    var map = HashMap<Int, Int>()
//    for(num in nums){
//        map.put(num, map.getOrDefault(num,0) +1)
//    }
//
//    // This allows you to compare the value of the dictinoary
//    val pq = PriorityQueue { (_, value): Map.Entry<Int?, Int>,
//                             (_, value1): Map.Entry<Int?, Int> -> value1 - value }
//
//    // Add the map entry to the queue
//    map.entries.forEach{
//        pq.add(it)
//    }
//    // Start popping from here on
//    var res = IntArray(k)
//    for(i in 0 until k){
//         pq.poll().key?.let{
//             res[i] = it
//         }
//    }
//    res.forEach{
//        println(it)
//    }
//    return res
//}
//
//fun Tree.Tree.Top6.Backtracking.Tree.Hard.Graph.Edges_question.Sliding_window.maining_window.Sliding_window.Graph.Hard.main(){
//    var nums = intArrayOf(4, 3, 3, 3, 3, 2, 1, 2)
//    topKMostFrequentElements(nums, 2)
//}