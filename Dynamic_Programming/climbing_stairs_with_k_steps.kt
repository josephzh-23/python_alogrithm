package Dynamic_programming

// What if we can climb a stairs with up to k steps
// More than 1 steps here
fun climbStairsWithKSteps(n: Int, k: Int): Int {
    if (n == 1) {
        return 1
    }
    val dp = IntArray(n + 1)
    dp[1] = 1
    dp[2] = 2

    // The solution here is that
    // dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + ... + dp[i-k]

    // dp[i] = dp[i-1] + dp[i-2] + dp[i-3]+ ... dp[i-k]
    for (i in 3..n) {
        for(j in 2 until k ) {
           if(i -j< 0){
               continue
           }else{
               dp[i] +=dp[i-j]
           }
        }
    }
    return dp[n]
}