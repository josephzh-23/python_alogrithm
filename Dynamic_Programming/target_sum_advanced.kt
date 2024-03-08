fun findTargetSumWaysBetter(nums: IntArray, target: Int): Int {
    return tways(nums, target, 0, HashMap())
}

fun tways(nums: IntArray, target: Int, curr: Int, memo: HashMap<String?, Int?>): Int {
    if (curr >= nums.size) {
        return if (target != 0) 0 else 1
    }
    val currkey = Integer.toString(curr) + "_" + Integer.toString(target)
    if (memo.containsKey(currkey)) return memo[currkey]!!
    val pos = tways(nums, target - nums[curr], curr + 1, memo)
    val neg = tways(nums, target + nums[curr], curr + 1, memo)
    memo[currkey] = pos + neg
    return memo[currkey]!!
}