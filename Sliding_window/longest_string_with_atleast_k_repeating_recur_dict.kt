package Sliding_window// The answer for this would be O(n^2) solution
// S: O(n)  the answer for this would be O(n^2)


fun main() {
    var word = "ababbc"
    longestSubstringWithAtLeastK(word, 2)
}

fun longestSubstringWithAtLeastK(s: String, k: Int): Int {
    val map: MutableMap<Char, Int> = HashMap()
    val str = s.toCharArray()
    for (c in str) {
        val index = c.code - 'a'.code
        map[c] = map.getOrDefault(c, 0) + 1
    }
    // Use this valid to indicate if false or true
    // freq[char] < k       then not valid
    var valid = true
    var start = 0
    var maxLen = 0
    for (end in 0 until s.length) {
        // TC -> O(N2)

        // We can do a split here
        // This is the point of split if below = true
        // in above case it would be c
        if (map[str[end]] in 1 until k) {
            println(str[end])
            val subString = s.substring(start, end)

            // Check for the 1st part of string after split
            maxLen = Math.max(maxLen,
                longestSubstringWithAtLeastK(subString, k)
            )

            // Check for 2nd part of str after split
            // a a b b c d e f
            // so it would take def if spliting at c
            start = end + 1
            valid = false
        }
    }
    return if (valid) {
        s.length
        // Not valid anymore
    } else {
        Math.max(maxLen, longestSubstringWithAtLeastK(s.substring(start), k))
    }
}

