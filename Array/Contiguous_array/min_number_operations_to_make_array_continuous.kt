package Array.Contiguous_array

import java.util.*

// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/description/

// Given you the minimum here
/*
1. Loop through every element as if it's the minimum element of possible can
didate here

2. When the element is in the range of curElement + (lenght - i)
increase the iwndow
 */

fun main() {
    var nums = intArrayOf(4, 2, 5, 3)
    minOperations(nums)
}
var maximum = 0
fun minOperations(nums: IntArray): Int {
    var length = nums.size
    nums.sort()
    var (start, end, max) = intArrayOf(0, 0, Int.MAX_VALUE)
    for (start in 0 until max) {
        while (nums[end] < nums[start] + length && end < nums.size) {
            end += 1
        }
        val candidateCount = end - start
        maximum = Math.max(maximum, candidateCount)
    }
    return length - max
}