// fill
fun main() {
    var arr = arrayOf(intArrayOf(0, 0, 0),
    intArrayOf(0, 1,0),
    intArrayOf(0,0, 0))
    println(uniquePathsWithObstacles(arr))
}
fun uniquePathsWithObstacles(g: Array<IntArray>): Int {
    val rows = g.size
    val cols = g[0].size
    var dp =  Array(rows) { IntArray(cols) }
    var flag = false

    /*
     If there is a obst in first row, every thing in first row
     becomes 1 or if there is a
     */

    for(i in 0 until cols){
        // this traverses the first row here
        if(flag || g[0][i] == 1){
            flag = true
            dp[0][i] = 0
        }else{
            dp[0][i] = 1
        }
    }

    flag = false

    // Everything in that first column will then be 0
    // If there is a zero there
        // [0][0]
        // [1][0]
    for(i in 0 until rows) {
        if(flag || g[i][0] == 1){
            flag = true
            dp[i][0] = 0
        }else{
            dp[i][0] = 1
        }
    }


    // Starting from cell(1,1) fill up the values
    // Unless the cell is 0 otherwise
    // No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
    // i.e. From above and left.
    for (i in 1 until rows) {
        for (j in 1 until cols) {
            if (g[i][j] == 0) {

                // we can check if this is a subsequence here or not
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            } else {
                dp[i][j] = 0
            }
        }
    }

    // Return value stored in rightmost bottommost cell. That is the destination.
    return dp[rows-1][cols-1]
}
