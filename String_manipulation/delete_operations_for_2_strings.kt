package String_manipulation

fun minDistance(text1: String, text2: String): Int {
    val dp = Array(text1.length + 1) { IntArray(text2.length + 1) }
    for (i in 0..text1.length) {
        for (j in 0..text2.length) {
            if (i == 0 || j == 0) {
                dp[i][j] = i + j
            } else if (text1[i - 1] == text2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1]
            } else {
                dp[i][j] = 1 + Math.min(dp[i - 1][j], dp[i][j - 1])
            }
        }
    }
    return dp[text1.length][text2.length]
}