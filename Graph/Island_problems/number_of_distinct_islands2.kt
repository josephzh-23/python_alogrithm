package Graph.Island_problems

import java.util.*


fun main() {

    var s = Solution333()
    var arr = arrayOf(intArrayOf(1, 1, 0, 0, 0),
            intArrayOf(1, 0, 0, 0, 0), intArrayOf(0, 0, 0, 0, 1))

    s.numDistinctIslands2(arr)
    println(s)
}

internal class Solution333 {
    private val directions = arrayOf(intArrayOf(1, 1), intArrayOf(-1, -1), intArrayOf(1, -1), intArrayOf(-1, 1))
    fun numDistinctIslands2(grid: Array<IntArray>): Int {
        val row = grid.size
        val col = grid[0].size
        val result: MutableSet<String?> = HashSet()
        for (i in 0 until row) {
            for (j in 0 until col) {
                if (grid[i][j] != 1) continue
                val path: MutableList<Point> = ArrayList()
                dfs(grid, i, j, path, row, col)
                path.forEach{
                    println("${it.x} and ${it.y}")
                }
                result.add(normalize(path))
            }
        }
        return result.size
    }

    private fun normalize(path: List<Point>): String? {
        val allShape: Array<MutableList<Point>> = Array(8){ mutableListOf<Point>()}
        for (i in 0..3) {
            allShape[i] = ArrayList()
            allShape[i + 4] = ArrayList()
            for (p in path) {
                allShape[i].add(Point(p.x * directions[i][0], p.y * directions[i][1]))
                allShape[i + 4].add(Point(p.y * directions[i][1], p.x * directions[i][0]))
            }
            Collections.sort(allShape[i])
            Collections.sort(allShape[i + 4])
        }
        val result = arrayOfNulls<String>(8)
        for (i in 0..7) {
            val x = allShape[i][0].x
            val y = allShape[i][0].y
            val sb = StringBuilder()
            for (p in allShape[i]) {
                sb.append(p.x - x)
                sb.append(',')
                sb.append(p.y - y)
                sb.append('/')
            }
            result[i] = sb.toString()
        }
        Arrays.sort(result)
        return result[0]
    }

    private fun dfs(grid: Array<IntArray>, i: Int, j: Int, path: MutableList<Point>, row: Int, col: Int) {
        if (i < 0 || i >= row || j < 0 || j >= col || grid[i][j] != 1) return
        grid[i][j] = 2
        path.add(Point(i, j))
        dfs(grid, i + 1, j, path, row, col)
        dfs(grid, i - 1, j, path, row, col)
        dfs(grid, i, j + 1, path, row, col)
        dfs(grid, i, j - 1, path, row, col)
    }
}

private class Point : Comparable<Point?> {
    var x = 0
    var y = 0

    constructor() {}
    constructor(x: Int, y: Int) {
        this.x = x
        this.y = y
    }

    override fun compareTo(p: Point?): Int {
        return if (x == p?.x) Integer.compare(y, p.y) else Integer.compare(x, p!!.x)
    }


}