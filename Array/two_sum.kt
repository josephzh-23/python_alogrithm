package Array


/*

It turns out we can do it in one-pass. While we are iterating and
inserting elements into the hash table, we also look back to check if current element's complement already exists in the hash table.
If it exists, we have found a solution and return the indices immediately.

https://leetcode.com/problems/two-sum/description/
 */


// 1 pass solution

fun twoSum(nums: IntArray, target: Int): IntArray? {
    val map: MutableMap<Int, Int> = HashMap()
    for (i in nums.indices) {
        val complement = target - nums[i]

        // Here we check if it's contained already as if we have already seen it
        if (map.containsKey(complement)) {
            return intArrayOf(map[complement]!!, i)
        }
        map[nums[i]] = i
    }
    // In case there is no solution, we'll just return null
    return null
}
