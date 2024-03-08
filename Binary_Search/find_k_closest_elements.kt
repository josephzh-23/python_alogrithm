package Binary_search

import java.util.*


/*

Bsically we just have to find the left boundary here

k: is the range here    x== the target
left boundary here

So we have 0... m ... (n-k) .... n
We only have to check in
0... m ... (n-k)


Our goal is basically find
A[mid] ___ x___ A[mid + k]
the x between the 2 values above here

Case 1:
So we have a bunch of cases here
x - A[mid] < A[mid + k] -x
need to move window to the left here

Case 2:
x - A[mid] > A[mid + k] -x
need to move window to the right here
 */


internal class Solution {
    fun findClosestElements(arr: IntArray, k: Int, x: Int): List<Int> {
        var left = 0
        var right = arr.size - k
        while (left < right) {
            val mid = (left + right) / 2
            if (x - arr[mid] > arr[mid + k] - x) {
                left = mid + 1
            } else {
                right = mid
            }
        }
        val res: MutableList<Int> = LinkedList()
        for (i in left until left + k) {
            res.add(arr[i])
        }
        return res
    }
}