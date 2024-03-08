package Array


internal class Solution(w: IntArray) {
    private val prefixSums: IntArray
    private val totalSum: Int

    init {
        prefixSums = IntArray(w.size)
        var prefixSum = 0
        for (i in w.indices) {
            prefixSum += w[i]
            prefixSums[i] = prefixSum
        }
        totalSum = prefixSum
    }

    fun pickIndex(): Int {
        val target = totalSum * Math.random()

        // run a binary search to find the target zone
        var low = 0
        var high = prefixSums.size
        while (low < high) {
            // better to avoid the overflow
            val mid = low + (high - low) / 2
            if (target > prefixSums[mid]) low = mid + 1 else high = mid
        }
        return low
    }
}