package String


// Sliding window

/*
Very similar to the porblem miminum window susbtring here

s2 contains permutation of s1

Satisfy the condition where the 2nd window contains the one we want
update the values that we want here

https://leetcode.com/problems/permutation-in-string/description/

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
 */

fun checkInclusion(t: String, s: String): Boolean {
    val map = IntArray(26)
    val arr = s.toCharArray() //Set up the table
    for (cur in t.toCharArray()) {
        map[cur.toInt()]++
    }
    var countAllCharInT = 0
    var left = 0
    val n = arr.size
    var right = 0
    while (right < n) {
        //Expand the window
        map[arr[right] -'a']--
        if (0 <= map[arr[right]- 'a']) {
            countAllCharInT++
        }

        //Shrink the window if current window contains all the char in t
        while (countAllCharInT == t.length) { //Update the minLen
            if (right - left + 1 == t.length) {
                return true
            }

            //Shrink the window
            map[arr[left]-'a']++
            if (0 < map[arr[left] -'a']) {
                countAllCharInT--
            }
            left++
        }
        right++
    }
    return false
}


