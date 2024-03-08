package Dynamic_programming

// We will skip the arr positions marked by false
/*
You are climbing a stairs, taking n steps to reach to the tops
Each time you can climb here, not allowed to step on red stairs
 */
fun climbStairsSkippingRed(n: Int, stairs: BooleanArray): Int {
    if (n == 1) {
        return 1
    }
    val dp = IntArray(n + 1)
    dp[1] = 1
    dp[2] = 2
    for (i in 3..n) {
        dp[i] = dp[i - 1] + dp[i - 2]
        if (stairs[i - 1]) {
            dp[i]= 0
        }else{
            dp[i] += dp[i]
        }
    }
    return dp[n]
}