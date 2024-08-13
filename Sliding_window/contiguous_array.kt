package Sliding_window.Basic

fun contiguousArray(nums: IntArray, k: Int): Boolean {
    // abs(i - j) <= k

    // Use hp to keep a slinding window here of size k
    val hp: MutableMap<Int, Int> = HashMap()
    // And do this here
    for( i in 0 until nums.size){
        // and then here when you have something
        if(hp.contains(nums[i])) return true
        hp[i] = nums[i]
        if(hp.size > k){
            hp.remove(nums[i-k])
        }
    }
    return false
}