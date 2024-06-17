import January_3rd.print
import java.util.*


fun main() {
    var arr = arrayOf(intArrayOf(0, 0, 0, 0, 0), intArrayOf(1, 1, 0, 0, 1), intArrayOf(0, 0, 0, 0, 0), intArrayOf(0, 1, 0, 0, 1), intArrayOf(0, 1, 0, 0, 0))

    var ball = intArrayOf(4, 3)
    var hole = intArrayOf(0, 1)
    findShortestWay(arr, ball, hole).print()

}


fun findShortestWay(maze: Array<IntArray>, ball: IntArray, hole: IntArray): String {
    val pq: PriorityQueue<Point> = PriorityQueue { a: Point, b: Point ->

        // this is used for lexicological order

        /*

        There are two shortest ways for the ball to drop into the hole.
The first way is left -> up -> left, represented by "lul".
The second way is up -> left, represented by 'ul'.

Both ways have shortest distance 6, but the first way
 is lexicographically smaller because 'l' < 'u'. So the output is "lul".
         */
        if (a.distance == b.distance)
//
//            // What if we don't use the following here
            a.movement.compareTo(b.movement) else a.distance - b.distance
    }


    val visited = Array(maze.size) { BooleanArray(maze[0].size) }
    val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
    val move = charArrayOf('d', 'u', 'r', 'l')

    pq.offer(Point(ball[0], ball[1], 0, ""))
    while (!pq.isEmpty()) {
        val point: Point = pq.poll()
        if (point.row == hole[0] && point.col == hole[1]) return point.movement
        visited[point.row][point.col] = true

        for (i in 0..3) {
            val dir = dirs[i]
            var row: Int = point.row
            var col: Int = point.col
            var distance: Int = point.distance
            while (isValid(maze, row + dir[0], col + dir[1])) {
                row += dir[0]
                col += dir[1]
                distance++
                if (row == hole[0] && col == hole[1]) break
            }
            if (!visited[row][col]) pq.offer(Point(row, col, distance, point.movement + move[i]))
        }
    }
    return "impossible"
}

fun isValid(maze: Array<IntArray>, row: Int, col: Int): Boolean {
    return if (row < 0 || row >= maze.size || col < 0 || col >= maze[0].size || maze[row][col] == 1) false else true
}

private class Point(var row: Int, var col: Int, var distance: Int, var movement: String)