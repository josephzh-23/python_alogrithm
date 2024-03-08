package Prefix_Sum


// https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/
/*

Formula: prefixSum[i] = arr[0] + arr[1] ... arr[i]
 */

// Can be used to find maximum subarray sum
// We already have this somewhere in the code

// Also in the dynamic programming solution here


// Function to compute maximum
// subarray sum in linear time.
fun maximumSumSubarray(arr: IntArray, n: Int): Int {
    // Initialize minimum
    // prefix sum to 0.
    var min_prefix_sum = 0

    // Initialize maximum subarray
    // sum so far to -infinity.
    var res = Int.MIN_VALUE

    // Initialize and compute
    // the prefix sum array.
    val prefixSum = IntArray(n)

    // Used to get the prefix sum array here
    prefixSum[0] = arr[0]
    for (i in 1 until n) prefixSum[i] = (prefixSum[i - 1] + arr[i])

    // loop through the array, keep
    // track of minimum prefix sum so
    // far and maximum subarray sum.
    for (i in 0 until n) {

        /*
        By - minPrefixSum, you will get what you want here
         */
        res = Math.max(res, prefixSum[i] - min_prefix_sum)
        min_prefix_sum = Math.min(min_prefix_sum,
                prefixSum[i])
    }
    return res
}

// Driver Program
fun main(args: Array<String>) {
    // Test case 1
    val arr1 = intArrayOf(-2, -3, 4, -1, -2, 1, 5, -3)
    val n1 = arr1.size
    println(maximumSumSubarray(arr1, n1))

    // Test case 2
    val arr2 = intArrayOf(4, -8, 9, -4, 1, -8, -1, 6)
    val n2 = arr2.size
    println(maximumSumSubarray(arr2, n2))
}