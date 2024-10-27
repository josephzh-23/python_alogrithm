package Pairs

https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/

'''
Problem statement

Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized.
Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j,
 the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

 Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5.
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.



The solution to solving this is using binary search here

1. Sort the array first and then
'''
// Minimize maximum difference between pairs
fun minimizeMax(nums: IntArray, p: Int): Int {

    nums.sort()
    var left = 0
    var right = INT_MAX

    while (left < right) {
        var mid = (left + right) / 2
        if (isOk(nums, p, mid)) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return left
}

fun isOk(nums: IntArray, p: Int, diff: Int): Boolean {
    var count = 0
    var n = nums.size
    var i = 0
    while (i in 0 until n) {
        if (i + 1 < n && nums[i + 1] - nums[i] <= diff) {
            count++
            i++
        }
    }
    return count >= p
}
