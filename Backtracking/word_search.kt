package Backtracking


//https://leetcode.com/problems/word-search/
internal class Solution {
    lateinit var matrix: Array<CharArray>
    lateinit var letters: CharArray
    lateinit var visited: Array<BooleanArray>
    fun exist(board: Array<CharArray>, word: String): Boolean {
        val rowLen = board.size
        val colLen = board[0].size
        letters = word.toCharArray()
        matrix = board
        for (i in 0 until rowLen) {
            for (j in 0 until colLen) {
                // If this is the first match of the letter
                // For each match we will have new visited array
                if (matrix[i][j] == letters[0]) {
                    visited = Array(rowLen) { BooleanArray(colLen) }
                    val res = dfs(i, j, 0)
                    if (res == true) return true
                }
            }
        }
        return false
    }

    private fun dfs(curRow: Int, curCol: Int, curIndex: Int): Boolean {
        //base cases
        println("the current index is $curIndex")
        if (curIndex == letters.size) return true
        if (curRow < 0 || curRow >= matrix.size) return false
        if (curCol < 0 || curCol >= matrix[0].size) return false

        // meaning if already visited
        if (visited[curRow][curCol]) return false
        if (matrix[curRow][curCol] != letters[curIndex]) return false

        // All conditions fulfilled
        visited[curRow][curCol] = true
        //Graph.Edges_question.dfs for all 4 dirctions
        val top = dfs(curRow - 1, curCol, curIndex + 1)
        val down = dfs(curRow + 1, curCol, curIndex + 1)
        val left = dfs(curRow, curCol - 1, curIndex + 1)
        val right = dfs(curRow, curCol + 1, curIndex + 1)

        // Then we need to return
        val ans = top || down || left || right

        // This is where we backtrack basically we change the visited
        // to unvisited here
        if (ans == false) {
            visited[curRow][curCol] = false
        }
        return ans
    }
}

fun main() {
    var s = Solution()
//    s.exist()
}
/**
[["A","B","C","E"],
["S","F","E","S"],
["A","D","E","E"]]
"ABCESEEEFS"
 **/