package Split

/*
https://leetcode.com/problems/split-array-largest-sum/description/

This is a hard question here
The largest sum of any subarray is minimized here
Say the array is [7, 2, 5, 10, 18]
m = 3       need to split into 3 here

l = max(nums) = 18
r = sum(nums) = 37
mid = (18 + 37) /2  = 27 here       the mid has to be between one of these 2 here

eturn the minimized largest sum of the split
 */

var m = 0       // m is the global max # of sums you can do around here
fun splitArrayLargestSum(nums: IntArray, m: Int): Int {


    var (l, r) = Pair(nums.max(), nums.sum())
    var res = r
    if (l != null) {
        while (l!! <= r) {
            val mid = l + (r - l) / 2

            // mid has to be >= the max element in the array
            if (canSplit(nums, mid)) {

                // Once we get 27 we set res to 27, and then 26 will be the next one
                res = mid
                r = mid - 1
            } else {
                l = mid + 1
            }
        }
    }
    return res
}

fun canSplit(nums: IntArray, largest: Int): Boolean {

    var (subArray, curSum) = intArrayOf(0, 0)


    for (n in nums) {
        curSum += n

// If adding the current element make the sum > x then we have to split here
        if (curSum > largest) {
            subArray += 1

            // Set the sum to the current element so a new array is found
            curSum = n
        }
    }
    return subArray + 1 <= m
}