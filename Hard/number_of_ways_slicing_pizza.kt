package Hard


class number_of_ways_slicing_pizza() {

    var m = 51;
    var n = 51;
    var cuts = 11;
    val dp = Array(m) { Array(n) { IntArray(cuts + 1) } }

    fun count(r: Int, c: Int, cuts: Int, apples: Array<IntArray>): Int {

        if (cuts == 0) {

            // If there is some cuts there to be found there then that's 1 case
            // there
            if (apples[r][c] > 0) {
                dp[r][c][cuts] = 1
            } else {
                dp[r][c][cuts] = 0
            }
            return dp[r][c][cuts]
        }

        var rowSum = 0;
        var colSum = 0;

        // horizontal cuts here
        for (i in r + 1 until n) {
            // there is still cuts left
            if (apples[r][c] - apples[i][c] > 0 && apples[i][c] >= cuts) {
                colSum = (colSum + count(i, c, cuts - 1, apples))
            }
        }

        // vertical cuts
        for (j in c + 1 until m) {
            // there is still cuts left
            if (apples[r][c] - apples[r][j] > 0 && apples[r][c] >= cuts) {
                colSum = (colSum + count(r, j, cuts - 1, apples))
            }
        }

        dp[r][c][cuts] = rowSum + colSum
        return dp[r][c][cuts]
    }

    fun ways(pizza: Array<String>, k: Int): Int {
        for (i in 0 until dp.size) {
            for (j in 0 until dp[0].size) {
                for (l in 0 until dp[0][0].size) {
                    dp[i][j][l] = -1
                }
            }
        }
        m = pizza.size
        n = pizza[0].length

        // Same as the question above
        var apples: Array<IntArray> = Array(m + 1) { IntArray(m + 1) }
        // Start from the outside towards inside
        for (i in m - 1 downTo 0) {
            for (j in n - 1 downTo 0) {
                println("$i and $j")
                var temp = 0
                if ((pizza[i][j] == 'A')) {
                    temp = 1
                }
                apples[i][j] = apples[i + 1][j] + apples[i][j + 1] - apples[i + 1][j + 1] + temp
            }
        }

        var ans = count(0, 0, k - 1, apples)
        return ans
    }
}

fun main() {
    var s = number_of_ways_slicing_pizza()
    var s2 = arrayOf("A..", "AAA", "...")
    s.ways(s2, 3)
}