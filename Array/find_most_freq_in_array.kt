package Array


// can also do sort and then scan

// Do a hash to store the count
internal object GFG {
    fun mostFrequent(arr: IntArray, n: Int): Int {

        // Insert all elements in hash
        val hp: MutableMap<Int, Int> = HashMap()
        for (i in 0 until n) {
            val key = arr[i]
            if (hp.containsKey(key)) {
                var freq = hp[key]!!
                freq++
                hp[key] = freq
            } else {
                hp[key] = 1
            }
        }

        // find max frequency.
        var max_count = 0
        var res = -1
        for ((key, value) in hp.entries) {
            if (max_count < value) {
                res = key
                max_count = value
            }
        }
        return res
    }

    // Driver code
    @JvmStatic
    fun main(args: Array<String>) {
        val arr = intArrayOf(40, 50, 30, 40, 50, 30, 30)
        val n = arr.size
        println(mostFrequent(arr, n))
    }
}