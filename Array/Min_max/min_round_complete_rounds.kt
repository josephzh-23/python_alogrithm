package Array.Min_max

import Util.printList
import java.util.*


fun main() {
    minimumRoundsCompleteAllTasks(intArrayOf(2, 2, 3, 3, 2, 4, 4, 4, 4, 4))
}
fun minimumRoundsCompleteAllTasks(tasks: IntArray): Int {
    // # of times sth has appeaared and the value here
    var dict = mutableMapOf<Int, Int>()
    var min = 0
    val maxHeap = PriorityQueue<IntArray> { a, b -> b[0] - a[0] }

    for(task in tasks){
        if(dict[task] == null){
            dict[task] = 0
        }else{
            dict[task] = dict[task]!! + 1
        }
    }
    for(it in dict.entries){
        maxHeap.add(intArrayOf(it.key, it.value))
    }
    printList(maxHeap.toList())

    while(maxHeap.size > 0){
        val ans = maxHeap.poll()
        var (num, value)  = Pair(ans[0], ans[1])
        //2 here then here
        if(num > 3){
            num -= 3
            maxHeap.add(intArrayOf(num, value))
        }
        min++

    }
    println(min)
    return 0
}