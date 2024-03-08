package Prefix_Sum

/*

sumRange(i, j) = sum(j + 1) - sum(i)
O(n) pre-compuatation
O(1) since cumulative sum is cached here

S: O(n)
 */

fun answer(nums: IntArray) {
    var prefixSum = IntArray(nums.size)
    var cur = 0
    for(i in 0 until nums.size){
        prefixSum[i+1] = prefixSum[i] + nums[i]

    }

    fun sumRange(left: Int, right: Int): Int {
        return prefixSum[right + 1] - prefixSum[left]
    }
}