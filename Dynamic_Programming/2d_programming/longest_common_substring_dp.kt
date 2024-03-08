// See the notes and illustration
//
fun lcsBottomUp(s1: String, s2: String, n: Int, m: Int): Int {
    if (n == 0 || m == 0) {
        return 0
    }
    var lcs = 0
    val arr = Array(n + 1) { IntArray(m + 1) }
    for (i in 1..n) {
        for (j in 1..m) {
            // This is the case where we have sth in common
            // between the two letters in the case 1
            if (s1[i - 1] == s2[j - 1]) {
                arr[i][j] = 1 + arr[i - 1][j - 1]
                lcs = Math.max(lcs, arr[i][j])
            } else {

                arr[i][j] = 0
            }
        }
    }
    return lcs
}