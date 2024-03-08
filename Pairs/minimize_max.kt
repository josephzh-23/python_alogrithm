package Pairs

import org.openxmlformats.schemas.drawingml.x2006.chart.STCrosses.INT_MAX

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
