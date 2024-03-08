package Graph.Islands

// Isaldn group of 1
/*
Leetcode solutino       -> TC: O (R *c)
SC: O( R* C) -> the seen 2d boolean that we created + space by callstack
 */
// When it traverses in all direction


class Solution {
    lateinit var grid:Array<IntArray>
    lateinit var seen: Array<BooleanArray>


    fun maxAreaOfIsland(grid: Array<IntArray>): Int {
        this.grid = grid;
        val rowSize = grid.size
        val colSize = grid[0].size
        seen =   Array(rowSize) { BooleanArray(colSize) }

        var num = 0
        for (r in 0 until rowSize) {
            for (c in 0 until colSize) {
                    num = Math.max(num, area(r, c))
                }
            }

            print("answer is $num")

            return num
        }


    // Make this return count at each turn
    fun area(r: Int, c: Int) : Int{

        // check the r and c at each point , also return
        // Make sure not visited
        if (r >= grid.size || c >= grid[0].size || c < 0 || r < 0 || seen[r][c]
                ||grid[r][c] == 0
            ) {
            return 0
        }

        /*
        Max area of island here
         */
        // The case where grid[r][c] =='1' basically, to mark it as visited
        //mark it
        seen[r][c] = true
        // Then call Graph.Edges_question.dfs on each direction
        return (1 + area(r+1, c) + area(r-1, c)
                + area(r, c-1) + area(r, c+1));
    }

}

fun main(){
    var s = Solution()
    // Time for testing now

    var grid = arrayOf(intArrayOf(0,0,1,0,0,0,0,1,0,0,0,0,0),
    intArrayOf(0,0,0,0,0,0,0,1,1,1,0,0,0),
    intArrayOf(0,1,1,0,1,0,0,0,0,0,0,0,0),
    intArrayOf(0,1,0,0,1,1,0,0,1,0,1,0,0),
    intArrayOf(0,1,0,0,1,1,0,0,1,1,1,0,0),
    intArrayOf(0,0,0,0,0,0,0,0,0,0,1,0,0),
    intArrayOf(0,0,0,0,0,0,0,1,1,1,0,0,0),
    intArrayOf(0,0,0,0,0,0,0,1,1,0,0,0,0))

    s.maxAreaOfIsland(grid)
}