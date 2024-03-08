package Binary_search

import java.lang.Integer.min

fun main() {
    var arr = intArrayOf(3, 4, 5, 1, 2)
    findMin(arr)
}

// Extension funciton
fun findMin(nums: IntArray):Int {

    var l = 0;
    var r = nums.size - 1
    var res = nums[0]
    var index = Int.MAX_VALUE
    while (l <= r) {
        // the case [3, 4, 5]
        if (nums[l] < nums[r]) {
            res = min(res, nums[l])
            break
        }
        var m = (l + r) / 2
        res = min(res, nums[m])
        if (nums[m] >= nums[l]) {
            l = m + 1
        } else {
            r = m - 1
        }
    }
    return res
}








