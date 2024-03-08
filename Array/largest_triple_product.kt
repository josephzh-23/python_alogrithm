package Array

import Util.printList
import java.util.*

fun main(args : Array<String>) {
    // Call findMaxProduct() with test cases here

    val arr = arrayOf(1,2, 3, 4, 5)
    var res = findMaxProduct(arr)
    printList(res.toList())
}

fun findMaxProduct(arr: Array<Int>): Array<Int> {

    // Working on this problem now
    var prod3 = 1
    // output[i] =
    var minHeap = PriorityQueue<Int>()

    var output = Array(arr.size){1}
    for(i in arr.indices){
//        println(" the element is ")
        minHeap.add(arr[i])

        if(minHeap.size < 3){
            output[i] = (-1)
            continue
        }
        else{

            // If an extra elementint he heap, then we can pop it
            if(minHeap.size >3){
                minHeap.poll()
            }

            var temp = mutableListOf<Int>()
            for (j in minHeap.indices) {
                println("minheap is ${minHeap.peek()}")
                temp.add(minHeap.peek())
                output[i] *= minHeap.poll()
            }

            // We have to add it back so now it's available for the
            // next iteration here
            for (t in temp) {
                minHeap.add(t)
            }
        }
    }
    return output
}