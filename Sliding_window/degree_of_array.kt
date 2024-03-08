package Sliding_window

import java.util.*


/*
https://leetcode.com/problems/degree-of-an-array/
 */
/*
An array that has degree d, must have some element x occur d times.
So 1. need count dict
2. Right and left index dict
3.
 */
// for each elem, left: idx of 1st occur
// right: idx of last occur

// nums = [1,2,3,2,5] we have left[2] = 1 and right[2] = 3.
/*
For each elem x that occurs, the maximum number of times
will be  right[x] - left[x] + 1
 */
fun degreeOfArray(nums: IntArray): Int {

    // Get the left most position of each element
    // So if [1, 2, 2, 3]
    // This will store left[2] = 1 instead of 2
    val left: MutableMap<Int, Int> = HashMap<Int, Int>()

    // Get the right most position of each element
    // So if [1, 2, 2, 3]
    // This will store left[2] = 2 instead of 1
    val right: MutableMap<Int, Int> = HashMap<Int, Int>()
    val count: MutableMap<Int, Int> = HashMap<Int, Int>()
    for (i in nums.indices) {
        val x = nums[i]
        // Initialize the left once and that's it
        // left[1] =
        if (left[x] == null) {
            left[x] = i
        }
        right[x] = i
        count[x] = count.getOrDefault(x, 0)!! + 1
    }
    var ans = nums.size

    // this will give max
    val degree = Collections.max(count.values)

    // Go thru its keys here
    for (x in count.keys) {

        if (count[x] == degree) {
            /*
            For each elem x that occurs, the maximum number of times
    will be  right[x] - left[x] + 1
             */
            ans = Math.min(ans, right[x]!! - left[x]!! + 1)
        }
    }
    println(2)
    return ans
}


fun main() {

    val arr = intArrayOf(1, 2, 2, 3, 1)
    degreeOfArray(arr)
}


