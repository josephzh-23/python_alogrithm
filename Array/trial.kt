package Array

import java.util.*

fun main() {
    // And then here we have the building
    var heights = intArrayOf(4, 3, 2, 1)
    findBuildings(heights)

}

fun findBuildings(heights: IntArray) {
    var stack = Stack<Int>()
//    var result = mutableListOf<Int>()
    for (i in heights.indices) {
        /*
               Cond 1:
               If the next element is greater than the arr[stack.peek()]
               then pop the top of the stack till we find a equal or greater element.
             */
        while (!stack.isEmpty() && heights[stack.peek()] < heights[i]) stack.pop()

        if (stack.isEmpty()) {
//            result.add(i)
        }
        stack.push(i)
    }
    println(stack)
}