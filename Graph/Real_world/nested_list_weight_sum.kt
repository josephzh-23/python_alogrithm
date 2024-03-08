package Graph.Real_world

import java.util.*


class NestedInteger {
    // Constructor initializes an empty nested list.
    constructor()

    // Constructor initializes a single integer.
    constructor(value: Int)

    // @return true if this NestedInteger holds a single integer, rather than a nested list.
    fun isInteger(): Boolean = false

    // @return the single integer that this NestedInteger holds, if it holds a single integer
    // Return null if this NestedInteger holds a nested list
    fun getInteger(): Int? {
        return 0
    }

    // Set this NestedInteger to hold a single integer.
    fun setInteger(value: Int): Unit {

    }

    // Set this NestedInteger to hold a nested list and adds a nested integer to it.
    fun add(ni: NestedInteger): Unit {}

    // @return the nested list that this NestedInteger holds, if it holds a nested list
    // Return null if this NestedInteger holds a single integer
    fun getList(): List<NestedInteger>? {
        return emptyList()
    }
}

/*
 Example here
 [[1, 1], 2, [1, 1]]
 if you see the above, add [1, 1] to the back so it
 can be processed later here
 q = [2, [1, 1 , 1, 1]]

    */

// How the queue is then added here
fun depthSum(nestedList: List<NestedInteger?>?): Int {
    val queue: Queue<NestedInteger> = LinkedList()
    queue.addAll(nestedList!!)
    var depth = 1
    var total = 0
    while (!queue.isEmpty()) {
        val size = queue.size
        for (i in 0 until size) {
            val nested = queue.poll()
            if (nested.isInteger()) {
                total += nested.getInteger()!! * depth
            } else {
                queue.addAll(nested.getList()!!)
            }
        }
        depth++
    }
    return total
}