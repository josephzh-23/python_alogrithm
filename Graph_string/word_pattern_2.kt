package String.Match


class Solution {
    fun wordPatternMatch(pattern: String, str: String): Boolean {
        val map: MutableMap<Char, String?> = HashMap()
        val set: MutableSet<String> = HashSet()
        return isMatch(str, 0, pattern, 0, map, set)
    }

    fun isMatch(
        str: String, i: Int, pat: String, j: Int, map: MutableMap<Char, String?>, set: MutableSet<String>
    ): Boolean {
        // base case
        if (i == str.length && j == pat.length) return true
        if (i == str.length || j == pat.length) return false

        // get current pattern character
        val c = pat[j]

        // if the pattern character exists
        if (map.containsKey(c)) {
            val s = map[c]

            // then check if we can use it to match str[i...i+s.length()]
            // Case 1 we can't match here
            return if (!str.startsWith(s!!, i)) {
                false
            } else isMatch(str, i + s.length, pat, j + 1, map, set)

            // if it can match, great, continue to match the rest
        }

        // pattern character does not exist in the map
        for (k in i until str.length) {
            val p = str.substring(i, k + 1)
            if (set.contains(p)) {
                continue
            }

            // create or update it
            map[c] = p
            set.add(p)

            // continue to match the rest
            if (isMatch(str, k + 1, pat, j + 1, map, set)) {
                return true
            }

            // backtracking
            map.remove(c)
            set.remove(p)
        }

        // we've tried our best but still no luck
        return false
    }
}