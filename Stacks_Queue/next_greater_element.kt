package Stacks_Queue

import java.util.*

/*
This is the better solution using an O (n + m) here

We will use a monotonic stack here
 */

/*
In stack when you have
if n1 = [4, 1, 2]
n2 = [2, 1, 3, 4]

and then you add 2, 1 to

 */
fun nextGreaterElement(nums1: IntArray, nums2: IntArray): IntArray {


    // We have the index to itself here
    var num1Index = mutableMapOf<Int, Int>()
    nums1.forEachIndexed { it, idx ->
        num1Index[it] = idx
    }
    var stack = Stack<Int>()
    var res = IntArray(nums1.size)
    for (i in nums2.indices) {
        var cur = nums2[i]/*
 n1 = [4, 1, 2]  stack = [2, 1]
 n2 = [2, 1, 3, 4]      if we see 3, then pop 1, and
 */
        while (stack.isNotEmpty() && cur > stack.pop()) {
            var value = stack.pop()
            var idx = num1Index[value] // where we have 1, we will replace with 3
            // res: [-1, 3, 3]
            res[idx!!] = cur
        }

        /*
       Everything here in the stack is in the increaseing order here
         */
        if (num1Index.contains(cur)) {
            stack.add(cur)
        }
    }
    return res
}