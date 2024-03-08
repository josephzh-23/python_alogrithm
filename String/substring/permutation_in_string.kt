package String.Sliding_window


/*
https://leetcode.com/problems/permutation-in-string/description/
Instead of generating the hashmap for every window, can create this once
for the first window only here

So we can have a sliding window iwth a map like before
 */

class Solution {
    fun checkInclusion(s1: String, s2: String): Boolean {
        if (s1.length > s2.length) return false
        val s1map = IntArray(26)
        val s2map = IntArray(26)
        for (i in 0 until s1.length) {
            s1map[s1[i].toInt() - 'a'.toInt()]++
            s2map[s2[i].toInt() - 'a'.toInt()]++
        }
        for (i in 0 until s2.length - s1.length) {
            if (matches(s1map, s2map)) return true
            s2map[s2[i + s1.length].toInt() - 'a'.toInt()]++
            s2map[s2[i].toInt() - 'a'.toInt()]--
        }
        return matches(s1map, s2map)
    }

    fun matches(s1map: IntArray, s2map: IntArray): Boolean {
        for (i in 0..25) {
            if (s1map[i] != s2map[i]) return false
        }
        return true
    }
}