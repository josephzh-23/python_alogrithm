package Graph.Island_problems

import Graph.Islands.directions
import January_3rd.print


fun dfs(grid: Array<CharArray>, r: Int, c: Int) {

    val nr = grid.size
    val nc = grid[0].size


    // Set up a return statement
    if (r < 0 || c < 0 || r >= nr || c >= nc || grid[r][c] == '0') {
        // Then here
        return
    }
    // once visited have to do this
    grid[r][c] = '0'

//    Graph.Edges_question.dfs(grid, r - 1, c)
//    Graph.Edges_question.dfs(grid, r + 1, c)
//    Graph.Edges_question.dfs(grid, r, c + 1)
//    Graph.Edges_question.dfs(grid, r, c - 1)


    directions.forEach {
        dfs(grid, r + it[0], c + it[1])
    }

}

fun numberOfIslandsDfs(grid: Array<CharArray>): Int {

    // Fix the students here and then you can get the number of islsands heree
    // Fix the number of islands here

    if (grid == null || grid.size == 0) {
        return 0
    }
    var nr = grid.size
    var nc = grid[0].size

    var count = 0
    // ONce you get these 2 then go
    for (r in 0 until nr) {
        for (c in 0 until nc) {
            // And now it's even brighter here

            if (grid[r][c] == '1') {
                count++
                dfs(grid, r, c)
            }
        }
    }
    return count
}


// This solution has been tested as well
fun main() {
    var grid = arrayOf(
        charArrayOf('1', '1', '0', '0', '0'),
        charArrayOf('1', '1', '0', '0', '0'),
        charArrayOf('0', '0', '1', '0', '0'),
        charArrayOf('0', '0', '0', '1', '1')
    )


    numberOfIslandsDfs(grid).print()
    // and using this we can have the data sent here
}