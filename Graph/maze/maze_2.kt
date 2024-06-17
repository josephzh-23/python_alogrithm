package Graph.maze_3

import java.util.*

internal class Solution {
    var dirs = arrayOf(intArrayOf(-1, 0), intArrayOf(1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
    fun shortestDistance(maze: Array<IntArray>, start: IntArray, destination: IntArray): Int {
        val n = maze.size
        val m = maze[0].size
        val dist = Array(n) { IntArray(m) }
        for (i in 0 until n) {
            Arrays.fill(dist[i], Int.MAX_VALUE)
        }
        dist[start[0]][start[1]] = 0
        dijkstra(maze, start, destination, dist)
        return if (dist[destination[0]][destination[1]] == Int.MAX_VALUE) -1 else dist[destination[0]][destination[1]]
    }

    fun dijkstra(maze: Array<IntArray>, start: IntArray?, destination: IntArray, dist: Array<IntArray>) {
        val pq = PriorityQueue { a: IntArray, b: IntArray ->
            a[2] - b[2]
        }
        //inde 0 : x , index 1: y, indedx2 : the distance
        val n = maze.size
        val m = maze[0].size
        while (!pq.isEmpty()) {
            val cur = pq.poll()
            if (cur[0] == destination[0] && cur[1] == destination[1]) {
                return
            }
            for (dir in dirs) {
                var x = dir[0] + cur[0]
                var y = dir[1] + cur[1]
                var cur_step = 1
                while (x >= 0 && y >= 0 && x < n && y < m && maze[x][y] == 0) {
                    x += dir[0]
                    y += dir[1]
                    cur_step++
                }

                // You decrease by 1 and check the steps here
                x -= dir[0]
                y -= dir[1]
                cur_step--

                // If you have sth smaller than the previously store distance then yo uneed to update x
                // it as explained updat ethe distance here if not good enugh as said
                if (dist[cur[0]][cur[1]] + cur_step < dist[x][y]) {
                    dist[x][y] = dist[cur[0]][cur[1]] + cur_step
                    pq.add(intArrayOf(x, y, dist[x][y]))
                }
            }
        }
    }
}