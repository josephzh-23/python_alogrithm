package Dynamic_programming

/*

Given an integer array nums, find a subarray that has the
 largest product, and return the product.

 using dp to solve this problem [top down approach]

O (n)
O (1) not using array or dict or anythign at all
 */
/*
    For this you can visusalize as following
            2   -5     3    1     -4    0   -10     2    8
cur                         1
max_so_far                  3      120
min_so_far                  -30   -12
Since we have negative number
so as seen we need to keep track of the min and max seen so far
 */
/*
 use a curMin and curMax so far, and also keep track of the result so
 far, because the result could be either
 - arr[i] * arr[i-1] or just arr[i] itself at that point
 */


internal class Solution18 {
    fun maxProduct(nums: IntArray): Int {
        var max_so_far = nums[0]
        var min_so_far = nums[0]

        // As said this can just store the result but we need
        // to keep track of it as explained above
        var res = nums[0]
        val N = nums.size
        for (i in 1 until N) {

            // We need the temp stored here so far
            val tempMax = max_so_far
            max_so_far = Math.max(nums[i], Math.max(max_so_far * nums[i], min_so_far * nums[i]))
            min_so_far = Math.min(nums[i], Math.min(tempMax * nums[i], min_so_far * nums[i]))
            res = Math.max(res, max_so_far)
        }
        return res
    }
}

fun main() {
    var intarr = intArrayOf(2, 3, -2 , 4)

}






