package String.Sliding_window

import java.util.*


fun lengthOfLongestSubstringKDistinct(s: String, k: Int): Int {
    val n = s.length
    if (n * k == 0) {
        return 0
    }
    var left = 0
    var right = 0
    val rightmostPosition: MutableMap<Char, Int> = HashMap()
    var maxLength = 1
    while (right < n) {
        rightmostPosition[s[right]] = right++
        if (rightmostPosition.size == k + 1) {
            val lowestIndex = Collections.min(rightmostPosition.values)
            rightmostPosition.remove(s[lowestIndex])
            left = lowestIndex + 1
        }
        maxLength = Math.max(maxLength, right - left)
    }
    return maxLength
}

fun main() {
    lengthOfLongestSubstringKDistinct("eceba", 2)
}