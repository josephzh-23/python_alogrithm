//package Dynamic_programming
//
//
///*
//The recurrent relation here
//at each turn rob = max(arr[0] + rob[2: n], rob[1:n]
//so as shown above either
// 1. rob the 1st house, skip 2nd and then the rest
// 2. skips 1st, and then rob the rest
//
// [1  2  3  1]
//  1  2  4  4
//
//  The max is 4,
// */
//
//// rob only the 1 house
//fun rob(nums: IntArray): Int {
//
//    // At i= 1 ,or 0
//
//    var dp = IntArray(nums.size+ 1)
//    dp[i] = max(dp[i], dp[i-1]+ dp[i])
//}

class robHouse {
    fun rob(nums: IntArray?): Int {
        if (nums == null || nums.size == 0) {
            return 0
        }
        if (nums.size == 1) {
            return nums[0]
        }
        if (nums.size == 2) {
            return Math.max(nums[0], nums[1])
        }
        val dp = IntArray(nums.size)
        dp[0] = nums[0]
        dp[1] = Math.max(nums[0], nums[1])
        for (i in 2 until dp.size) {
            //It's either the value at index before or
            // the cur value + the value at 2 index before [i- 2]
            // in the example
            dp[i] = Math.max(nums[i] + dp[i - 2], dp[i - 1])
        }
        return dp[nums.size - 1]
    }
}