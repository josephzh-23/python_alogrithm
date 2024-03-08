package Array.Hard

import java.util.*

fun largestRectangleAreaStack(h: IntArray?): Int { //Check null condition
    if (h == null || h.size == 0) return 0

    //We want the stack here to be in increasing order as said
    val n = h.size

    // To store all the index of the variable that's greater here
    val stack: Stack<Int> = Stack()
    var maxArea = 0
    var i = 0
    while (i <= n) {
        val curHeight = if (i == n) 0 else h[i] //If stack is empty of ht >= h[top] push in stack

        if (stack.isEmpty() || curHeight >= h[stack.peek()]) {
            stack.push(i)

            // if curHeight < h[stack.peek]
        } else {
            //Process elements and find the mexArea for popped index
            val top: Int = stack.pop()

            println("the stacked peek is ")
            val width = if (stack.isEmpty()) i else i - stack.peek() - 1
            val area = h[top] * width
            maxArea = Math.max(maxArea, area)

            // Why -- here? we need to be at the previous position
            i--
        }
        i++
    }
    return maxArea
}