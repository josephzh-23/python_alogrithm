package Array

import java.util.*

/*
The question here is that the value at index i must be the max element
in the contiguous array
// 12321        3 being the maximum in the middle here
- the contiguous subarray must start or end on index i

 */

// Contiguous subarray problem here leetcode

/*

Maintain a stack : containing the index of the last element enecountered



 */

fun findCOuntOfContiguousSubarray(arr: IntArray) {

    val stack = Stack<Int>()

    val result = IntArray(arr.size)

    // for every index check from the left for possible array
    stack.push(0)
    for (i in arr.indices) {
        /*
                Cond 1:
                If the next element is greater than the arr[stack.peek()]
                then pop the top of the stack till we find a equal or greater element.
              */
        while (!stack.isEmpty() && arr[stack.peek()] < arr[i]) stack.pop()

        // After the last step the stack top is the max element and hence contiguous
        /*
        Cond 2:
        If stack empty: current elem is the biggest element here
        hence : there are (curindex + 1) possible arrays meeting the criteria
           */
        if (stack.isEmpty()) {
            result[i] = i + 1

            /*
            Cond 3:
            If stack is not empty, then (current index - stack top) will be possible arrays for the index position
            Repeat the same steps from end of the array to get the final solution.

             */
        } else {
            result[i] = i - stack.peek()
        }


        stack.push(i)
    }
    stack.clear()

// for every index check from the right for possible contiguous arrays
    stack.push(arr.size - 1)


    for (i in arr.size - 2 downTo 0) {
        while (!stack.isEmpty() && arr[stack.peek()] < arr[i]) stack.pop()
// after the above step either stack is empty or stack top is the max element and hence contiguous sub-arrays having max element at i are only possible till the stack top
        if (stack.isEmpty()) result[i] += arr.size - i - 1 else result[i] += stack.peek() - i - 1
        stack.push(i)
    }
    println(result)
}

