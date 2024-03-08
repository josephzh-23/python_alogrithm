/*

So there are 3 cases here

1. the last char matching
2. the second last char matching for either string 1 or
string 2 here
 */

fun lcsubstring(s1: String, s2: String, n: Int, m: Int, countOfLCS: Int): Int {
    var countOfLCS = countOfLCS
    if (n == 0 || m == 0) {
        return countOfLCS
    }

    // case 1
    if (s1[n - 1] == s2[m - 1]) {
        countOfLCS = lcsubstring(s1, s2, n - 1, m - 1, countOfLCS + 1)
    }
    // case 2 and 3
    val count1 = lcsubstring(s1, s2, n - 1, m, 0)
    val count2 = lcsubstring(s1, s2, n, m - 1, 0)
    return Math.max(countOfLCS, Math.max(count1, count2))
}



fun main(args: Array<String>) {
    val s1 = "abd"
    val s2 = "abca"
    println(lcsubstring(s1, s2, s1.length, s2.length, 0))
    println(lcsBottomUp(s1, s2, s1.length, s2.length))
}