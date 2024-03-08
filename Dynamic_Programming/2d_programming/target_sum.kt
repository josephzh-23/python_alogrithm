var count = 0
fun findTargetSumWays(nums: IntArray, S: Int): Int {
    calculate(nums, 0, 0, S)
    return count
}

fun calculate(nums: IntArray, i: Int, sum: Int, S: Int) {
    if (i == nums.size) {
        if (sum == S) {
            count++
        }
    } else {
        calculate(nums, i + 1, sum + nums[i], S)
        calculate(nums, i + 1, sum - nums[i], S)
    }
}
