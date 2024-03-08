

/*
Need to keep track of the expression wether it's + or *
Important 1:
 */
private val ans: MutableList<String> = ArrayList()
fun addOperators(s: String, target: Int): List<String> {
    dfs(0, "", 0, 0, s, target)
    return ans
}

/*
Path: the expression so far here
s: string for the next iteration here
 */
private fun dfs(i: Int, path: String, resSoFar: Long, prevNum: Long, s: String, target: Int) {
    if (i == s.length) {
        if (resSoFar == target.toLong()) ans.add(path)
        return
    }
    for (j in i until s.length) {
        if (j > i && s[i] == '0') break // Skip leading zero number
        val currNum = s.substring(i, j + 1).toLong()
        if (i == 0) {
            dfs(j + 1, path + currNum, currNum, currNum, s, target) // First num, pick it without adding any operator!
        } else {
            dfs(j + 1, "$path+$currNum", resSoFar + currNum, currNum, s, target)
            dfs(j + 1, "$path-$currNum", resSoFar - currNum, -currNum, s, target)

            /*
           So if we have *, then need to undo the previous opeartion here

           3 + 2 *4     prev number is 2 so resSoFar - prevNum
             */
            dfs(j + 1, "$path*$currNum", resSoFar - prevNum + prevNum * currNum, prevNum * currNum, s, target)
        }
    }
}