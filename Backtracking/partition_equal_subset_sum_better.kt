package Backtracking

//https://leetcode.com/problems/partition-equal-subset-sum/

internal class Solution13 {
    fun canPartition(nums: IntArray): Boolean {
        var totalSum = 0
        // find sum of all array elements
        for (num in nums) {
            totalSum += num
        }
        // if totalSum is odd, it cannot be partitioned into equal sum subset
        if (totalSum % 2 != 0) return false
        val subSetSum = totalSum / 2
        val n = nums.size
        val memo = Array(n + 1) { BooleanArray(subSetSum + 1) }
        return dfs(nums, n - 1, subSetSum, memo)
    }

    // We check if the subsetnetsum has already been solved or not
    fun dfs(nums: IntArray, index: Int, subSetSum: Int, memo: Array<BooleanArray>): Boolean {
        // Base Cases
        if (subSetSum == 0) return true
        if (index == 0 || subSetSum < 0) return false
        // check if subSetSum for given n is already computed and stored in memo

        if (memo[index][subSetSum] != null) return memo[index][subSetSum]

        // This is simliar to the question from before
        val result = dfs(nums, index - 1, subSetSum - nums[index - 1], memo) ||
                dfs(nums, index - 1, subSetSum, memo)
        // store the result in memo
        memo[index][subSetSum] = result
        return result
    }
}