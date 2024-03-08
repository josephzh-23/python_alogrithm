internal object GFG {
    // TC: O(n)
    // SC: O(n)
    fun mostFrequent(arr: IntArray, n: Int): Int {
        // Insert all elements in hash
        val hp: MutableMap<Int, Int> = HashMap()
        for (i in 0 until n) {
            val key = arr[i]
            // This can be simplifed using getOrDefault()
            hp.put(key, hp.getOrDefault(key, 0) +1)
        }
        hp.forEach{
            println(it.key)
            println(it.value)
        }
        // find max frequency.
        var maxCount = 0
        var res = -1
        for (it in hp.entries){
            if (maxCount < it.value) {
                res = it.key
                maxCount = it.value
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