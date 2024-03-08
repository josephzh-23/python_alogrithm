package Hard


/*
The idea here is to use the right hand rule
1. When run into an obstacle here, then we turn right
 */



fun main() {
    var s = S()
    var rooms = arrayOf(intArrayOf(1, 1, 1),
                intArrayOf(1, 1, 1),
                intArrayOf(1, 1,1))
    s.cleanRoom(s.robot)


}
internal class S {
    // going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
    var directions = arrayOf(intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(1, 0), intArrayOf(0, -1))
    var visited: MutableSet<Pair<Int, Int>?> = HashSet()
    var robot: Robot? = null
    fun goBack() {
        robot!!.turnRight()
        robot!!.turnRight()
        robot!!.move()
        robot!!.turnRight()
        robot!!.turnRight()
    }

    fun backtrack(row: Int, col: Int, d: Int) {
        visited.add(Pair(row, col))
        robot!!.clean()
        // going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        for (i in 0..3) {

            // 1%4 = 1      2%4 = 2     3%4 = 3
            // 4%4 = 0 over here
            val newD = (d + i) % 4
            val newRow = row + directions[newD][0]
            val newCol = col + directions[newD][1]
            if (!visited.contains(Pair(newRow, newCol)) && robot!!.move()) {
                backtrack(newRow, newCol, newD)
//                goBack()
            }
            // turn the robot following chosen direction : clockwise
            robot!!.turnRight()
        }
    }

    fun cleanRoom(robot: Robot?) {
        this.robot = robot
        backtrack(0, 0, 0)
    }
}