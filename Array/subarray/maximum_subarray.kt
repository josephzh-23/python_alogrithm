package Array.subarray

//https://leetcode.com/problems/maximum-subarray/
// Can refer to the notes
/*
Find subarray with biggest sum
 */
/*
TC: O(n)        SC: O(1)
2 integers here
currentSubarray
    will keep the running count of the current subarray we are focusing on.
maxSubarray
    will be our final return value. Continuously update it whenever we find a bigger subarray.

During iteration :
 1. Start with the 2nd elem, use the 1st one to init our variable
     If currentSubarray becomes negative, we know it isn't worth keeping, so throw it away.

 2. Remember to update maxSubarray every time we find a new maximum
    and return maxSubarray
 */
fun maxSubArray(nums: IntArray): Int {
    // Initialize our variables using the first element.
    var currentSubarray = nums[0]
    var maxSubarray = nums[0]

    // Start with the 2nd element since we already used the first one
    // to init our variable
    for (i in 1 until nums.size) {
        val num = nums[i]

        // If you run into negative how to skip?
        // If current_subarray is negative, throw it away. Otherwise, keep adding to it.
        currentSubarray = Math.max(num, currentSubarray + num)
        maxSubarray = Math.max(maxSubarray, currentSubarray)
    }
    return maxSubarray
}