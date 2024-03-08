package Hard
interface Robot {


    // returns true if next cell is open and robot moves into the cell.
    // returns false if next cell is obstacle and robot stays on the current cell.
    fun move(): Boolean

    // Robot will stay on the same cell after calling turnLeft/turnRight.
    // Each turn will be 90 degrees.
    fun turnLeft()
    fun turnRight()

    // Clean the current cell.
    fun clean()
}

