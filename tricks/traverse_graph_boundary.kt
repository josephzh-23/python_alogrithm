package tricks

fun taverseBoundary(g: Array<IntArray>) {
    val rows = g.size
    val cols = g[0].size

    var flag = false

    // goes over every item in the first row
    for (i in 0 until cols) {
        if (flag || g[0][i] == 1) {
            flag = true
        }
    }
    // traverse everything in 1st column
    for (i in 0 until rows) {
        if (flag || g[i][0] == 1) {
            flag = true
        }
    }
}