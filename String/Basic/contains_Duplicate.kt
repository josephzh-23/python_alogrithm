package String.Basic
/*
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
 */
//https://leetcode.com/problems/contains-duplicate-ii/description/
fun main() {
    var nums = intArrayOf(1, 2, 3, 1)
    var k = 3
    containsNearbyDuplicate(nums, k)
}
fun containsNearbyDuplicate(nums: IntArray, k: Int): Boolean {
        // abs(i - j) <= k

    // Use hp to keep a slinding window here of size k
    val hp: MutableMap<Int, Int> = HashMap()
    // And do this here
//    var diff = abs(
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