import January_3rd.print

/*

https://leetcode.com/problems/minimum-window-substring/description/
O(n + m)    this will be the end
S will be sth like the following
"ADOBECODEBANC"
t will be "ABC"
 */
fun minWindow(s: String, t: String): String {
    if (s == null || t == null || s.isEmpty() || t.isEmpty()) return ""
    val map = mutableMapOf<Char, Int>()

    // You need 3 indices here
    for (i in t.indices) {

        val c = t[i]
        map.apply {
            put(c, getOrDefault(c, 0) + 1)
        }
    }

    /*
    The count is is for keeoing track of how many letters are found based on the input
    t
     */
    var (i, j, count) = intArrayOf(0, 0, map.size)


    // This is for adjusting the min
    var (left, right, min) = intArrayOf(0, s.length - 1, s.length)

    // Check if the one can actually be found here
    var found = false

    while (j < s.length) {

        val endChar = s[j++]

        if (map.containsKey(endChar)) { // Decrement this value in 1
            map.put(endChar, map.getOrDefault(endChar, 0) - 1)
            if (map[endChar] == 0) count -= 1
        }

        if (count > 0) continue

        // We increase the start character
        while (count == 0) {
            val startChar = s[i++]

            // Found sth that's in the t word
            if (map.containsKey(startChar)) {
                map.apply {
                    put(startChar, getOrDefault(startChar, 0) + 1)
                    if (getOrDefault(startChar, 0) > 0) {

                        // Increase the count again at the
                        count += 1
                    }
                }
            }

            // this is where we have to make the update to the min length
            if ((j - i) < min) {
                left = i
                right = j
                min = j - i
                found = true

            }
        }
    }

    // This is the final answer here

    return if (!found) "" else s.substring(left - 1, right)
}

fun main() {
    var s = "adobecodebance"
    var t = "abc"
    minWindow(s, t).print()
}