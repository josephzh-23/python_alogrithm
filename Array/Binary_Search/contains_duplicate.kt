package Binary_search

import java.util.*


fun containsDuplicate(nums: IntArray): Boolean {
    Arrays.sort(nums)
    for (i in 0 until nums.size - 1) {
        if (nums[i] == nums[i + 1]) return true
    }
    return false
}