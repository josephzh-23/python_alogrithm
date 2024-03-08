package Prefix_Sum

import java.lang.Math.pow


/*
So here at the start you have

We will use prefix sum here

By fixing one point (A), we could use binary search to find another point (B).
We want to find a range of point B which satisfies the given condition (leftSum <= midSum <= rightSum)

1. If the point B is too left, the midSum will be too small
2. If the point B is too right, the rightSum will be too small

3. Kind of like finding the first and last position of element in sorted array here
 */

/*
Basically we have a [leftSum, midSum, satsified area, right Sum]
                            A       b left         b right
 */

var mod = pow(10.0, 9.0) + 7
fun waysToSplit(nums: IntArray) {

    val n = nums.size
    var res = 0 // prefix array find the sum here first
    val prefixSum = IntArray(n)

    prefixSum[0] = nums[0] // part 1 here
    for (i in 1 until n) prefixSum[i] = prefixSum[i - 1] + nums[i]

    for (i in 1 until n - 1) {
        if (prefixSum[i - 1] > (prefixSum[n - 1] - prefixSum[i - 1]) / 2) break

        var left = helper(prefixSum, prefixSum[i - 1], i, true)
        var right = helper(prefixSum, prefixSum[i - 1], i, false)

        if (left == -1 || right == -1) continue // none is found

        res = ((res + (right - left + 1) %mod) % mod).toInt()
    }

    println(res)
}


/*
Passing prefix sum
curSum is either the left or the right sum
 */

private fun helper(A: IntArray, curSum: Int, index: Int, searchLeft: Boolean): Int {
    val N = A.size
    var l = index
    var r = N - 2
    var res = -1
    while (l <= r) {
        val m = (r - l) / 2 + l
        val midSum = A[m] - A[index - 1]
        val rightSum = A[N - 1] - A[m]
        if (curSum <= midSum && midSum <= rightSum) {
            res = m
            if (searchLeft) r = m - 1 else l = m + 1
        } else if (curSum > midSum) {  // shrink left
            l = m + 1
        } else {  // shrink right
            r = m - 1
        }
    }
    return res
}