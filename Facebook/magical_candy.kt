package Facebook

import Util.printList
import java.util.*


fun main(args : Array<String>) {
    // Call findMaxProduct() with test cases here

    val arr = arrayOf(2, 1, 7, 4, 2)
    var res = magicalCandy(arr, 2)
//    printList(res.toList())
}

fun magicalCandy(arr: Array<Int>, k:Int) {


    // output[i] =
    var maxHeap = PriorityQueue<Int>(reverseOrder())
    var res = 0
    var output = Array(arr.size){1}
    for(i in arr.indices){
//        println(" the element is ")
        maxHeap.add(arr[i])
    }

    for(i in 0 ..k){
        val max = maxHeap.poll()
        res+= max
        var next = max/2
        println("next is $next")
        maxHeap.add(next)
    }

    println(res)
}