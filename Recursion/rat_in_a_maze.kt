
var numOfPath = 0
fun findPath(m: Array<IntArray>, n: Int): ArrayList<String> {
    val ans = ArrayList<String>()
    val visited = Array(n) { BooleanArray(n) }
    function(0, 0, m, m.size, m[0].size, "", ans, visited)
    if (ans.size == 0) {
        ans.add("-1")
    }
    return ans
}

fun function(i: Int, j: Int, arr: Array<IntArray>, n: Int, m: Int, str: String, ans: ArrayList<String>, visited: Array<BooleanArray>) {
    if (i < n && j < m && i >= 0 && j >= 0 && arr[i][j] != 0 && visited[i][j] == false) {

        //When it reaches here return and that's it it's done but if not then
        if (i == n - 1 && j == m - 1) {
            ans.add(str)
            return
        }
        visited[i][j] = true
        function(i + 1, j, arr, n, m, str + "D", ans, visited)
        function(i - 1, j, arr, n, m, str + "U", ans, visited)
        function(i, j + 1, arr, n, m, str + "R", ans, visited)
        function(i, j - 1, arr, n, m, str + "L", ans, visited)

        // This is for back tracking
        visited[i][j] = false
    } else {
        return
    }
}