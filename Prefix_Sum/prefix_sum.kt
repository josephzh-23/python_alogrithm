package Prefix_Sum


internal object Prefix {
    // Fills prefix sum array
    fun fillPrefixSum(arr: IntArray, n: Int,
                      prefixSum: IntArray) {
        prefixSum[0] = arr[0]
        // Adding present element with previous element
        for (i in 1 until n) prefixSum[i] = prefixSum[i - 1] + arr[i]
    }

    // Driver code
    @JvmStatic
    fun main(args: Array<String>) {
        val arr = intArrayOf(10, 4, 16, 20)
        val n = arr.size
        val prefixSum = IntArray(n)

        // Function call
        fillPrefixSum(arr, n, prefixSum)
        for (i in 0 until n) print(prefixSum[i].toString() + " ")
        println("")
    }
}