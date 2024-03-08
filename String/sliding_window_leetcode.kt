package String

internal class Solution {
    var deq = ArrayDeque<Int>()
    lateinit var nums: IntArray
    fun clean_deque(i: Int, k: Int) {
        // remove indexes of elements not from sliding window
        if (!deq.isEmpty() && deq.first() === i - k) deq.removeFirst()

        // remove from deq indexes of all elements
        // which are smaller than current element nums[i]
        while (!deq.isEmpty() && nums[i] > nums[deq.last()]) deq.removeLast()
    }

    fun maxSlidingWindow(nums: IntArray, k: Int): IntArray {
        val n = nums.size
        if (n * k == 0) return IntArray(0)
        if (k == 1) return nums

        // init deque and output
        this.nums = nums
        var max_idx = 0
        for (i in 0 until k) {
            clean_deque(i, k)
            deq.addLast(i)
            // compute max in nums[:k]
            if (nums[i] > nums[max_idx]) max_idx = i
        }
        val output = IntArray(n - k + 1)
        output[0] = nums[max_idx]

        // build output
        for (i in k until n) {
            clean_deque(i, k)
            deq.addLast(i)
            output[i - k + 1] = nums[deq.first()]
        }
        return output
    }
}