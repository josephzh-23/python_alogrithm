package String.substring

import java.lang.Integer.min



import java.lang.Integer.max

// A common substring between 2 strings
// text 1 = "abcde" and text2= "ace"
// longest common = "ace"

/*
    Case 1:
    Ex abcde    ex2: ace        a is a match at idx = 0

    if first lettter, both a match then break into subproblem + 1, so here it
    would be a
    -
    Case 2:
    bdcde       ace
    No match, so could be now beteween "dcde" "ace", by comparing
    1st, can break up problem and solve into
        a   c   e
    a
    b
    c
    d
    e
    Use a 2d to solve this problem here,
    For (a,a)   -> you need to find ans for other positions first
    before you work your way back up here.  ->

    There r 2 optiosn: either go diagonally or go right or go down
    Check(a,a) since equal go diagonal down,
     then check (b, c)

    0.Diagonal then go right or down
    1. if not equal don't go diagonal, then we go right or go down
    then we take the max of (right or down) and put it in the position before
    that we just came down from
 */




fun longestCommonSubsequence(text1: String, text2: String): Int {
    lateinit var dp: Array<IntArray>

    // Initialize an array of 0s
    dp = Array(text1.length + 1) { IntArray(text2.length + 1) }
    // We need to initialise the memo array to 0s so that we know
    // whether or not a value has been filled in. Keep the base cases
    // as 0's to simplify the later code a bit.

    // See if you can do without the following here
    for (i in 0 until text1.length) {
        for (j in 0 until text2.length) {
            dp[i][j] = 0
        }
    }

    // We will work up from the bottom of the matrix
    for (i in text1.indices.reversed()) {
        for (j in text2.indices.reversed()) {

            // This is the matching case so we add 1
            // to the diagnol situation from before
            // so we go diagonal
            if (text1[i] == text2[j]) {
                dp[i][j] = 1 + dp[i+1][j+1]
            } else {
                // you take the max
                dp[i][j] = min(dp[i][j+1], dp[i+1][j])
            }
        }
    }
    print(dp[0][0])
    return dp[0][0]
    // The result would be stored here at
}


fun main() {
    print(longestCommonSubsequence("abac", "cab"))
    // shoudl be ace
}


