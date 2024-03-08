package String

// Do the straightforwad solution
// O (n *k)         n # of elemn in array

    fun minSlidingWindow(nums: IntArray, k: Int): IntArray {
        val n = nums.size
        if (n * k == 0) return IntArray(0)

        // If [1 2 3 4 5]
        val output = IntArray(n - k + 1)

        // At each iter, i is increased
        for (i in 0 until n - k + 1) {
            var max = Int.MIN_VALUE
                /*
             j is the index for the sliding window
             [1 2 3 4 5]      if k = 3
             at the start woudl be [1 2 3]
            */

            for (j in i until i + k) max = Math.max(max, nums[j])

            /*
            if k = 3 would return [1 2 3]
             */
            output[i] = max
        }
        return output
    }