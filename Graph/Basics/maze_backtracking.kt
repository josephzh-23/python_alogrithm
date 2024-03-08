// The maze problem here done using backtracking here
fun main() {
    // Given a 4* 4 maze here
    val s = arrayOf(
        intArrayOf(1, 0, 0, 0), intArrayOf(1, 1, 0, 0),
        intArrayOf(1, 1, 0, 0), intArrayOf(0, 1, 1, 1)
    )
    // Have this here for that


    var s2 = Fin()
    s2.findPath2(s, 4).forEach {
        println(it)
    }
}


var hasPath = false

// 1 is the obstacle here and 0 is an open path

class Fin() {
    fun findPath2(m: Array<IntArray>, n: Int): ArrayList<String> {
        val ans = ArrayList<String>()

        // Visited here will be passed in automatically here
        val visited = Array(n) { BooleanArray(n) }


        // See what we get here
        function2(0, 0, m, m.size, m[0].size, ans, visited)
        println(hasPath)
        if (ans.size == 0) {
            ans.add("-1")
        }
        return ans
    }

    fun function2(
        i: Int,
        j: Int,
        arr: Array<IntArray>,
        n: Int,
        m: Int,
        ans: ArrayList<String>,
        visited: Array<BooleanArray>
    ) {
        // This is the if valid entry here
        if (i < n && j < m && i >= 0 && j >= 0 && arr[i][j] != 0 && visited[i][j] == false
            && hasPath == false) {

            if (i == n - 1 && j == m - 1) {

                println("came here")
                hasPath = true
                return
            }
            visited[i][j] = true
            function2(i + 1, j, arr, n, m, ans, visited)
            function2(i - 1, j, arr, n, m, ans, visited)
            function2(i, j + 1, arr, n, m, ans, visited)
            function2(i, j - 1, arr, n, m, ans, visited)

            // This is for back tracking
            visited[i][j] = false
        } else {
            return
        }
    }
}