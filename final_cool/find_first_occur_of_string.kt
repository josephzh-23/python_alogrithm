package final_cool

// O(n) solution here

// Find needle in the haystack problem leetcode

// Input: haystack = "sadbutsad",
// needle = "sad"               Above would be the input and then the output as shown
internal class Solution {
    fun strStr(haystack: String, needle: String): Int {
        val m = needle.length
        val n = haystack.length
        for (i in 0 until haystack.length - needle.length + 1) {
                if(haystack.get(i) == needle.get(i)){


                // Here can also use the haystack
                if(haystack.substring(i, needle.length + i).equals(needle)){
                    return i
                }
            }
        }
        return -1
    }
}








