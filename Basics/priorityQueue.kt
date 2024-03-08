package Util

import java.util.*
// Use this with a map behavior
/*
Finding max: O(1)      max always at the root 
For enqueing and dequeing methods,  O(log(n))   look at top k most frequent
elements here
For the remove(Object) and contains(Object) methods O(n)
For the retrieval methods, O(1)
 */
fun main(){

    // Prioirty queue by itself is a min queue it would seem
    var nums = intArrayOf(1, 2, 3, 4,4, 4, 4, 3)
    var map = HashMap<Int, Int>()
    for(num in nums){
        map.put(num, map.getOrDefault(num,0) +1)
    }
    var pq = PriorityQueue<Int>()
    pq.add(5)
    pq.add(4)
    pq.add(6)

    println(pq.poll())

}