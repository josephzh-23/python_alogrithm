package String.Hard

/*
https://leetcode.com/problems/regular-expression-matching/description/
s = "aa"
p = "a*"
    . means anything here
    * means 0 or more of the preceding element here
 */
fun isMatch(s: String, p: String): Boolean {

 return dfs(s, p, 0, 0)
}

fun dfs(s: String, p: String, i: Int, j: Int): Boolean {

    val (i, j) = Pair(i, j)
    if (i >= s.length && j >= p.length) {
        return true
    }
    if (j >= p.length) {
        return false
    }

    // Ensure a match for the 1st character here this
    // will be reused a couple of times here
    var match = i < s.length && (s[i] == p[j] || p[j] == '.')

    // For the start case
    if (j + 1 < p.length && p[j + 1] == '*') {

   // Can skip the star (j +2 ) ||
        return dfs(s, p, i, j + 2) ||
                //  use the star, add 1 to it leave that
                (match && dfs(s, p, i + 1, j))
    }

    // If 2 characters match then keep going
    if (match) {
        return dfs(s, p, i + 1, j + 1)
    }
    return false
}










