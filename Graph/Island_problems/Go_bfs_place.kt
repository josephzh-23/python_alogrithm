package Graph.Islands

import Graph.isInBoundsChar
import java.util.*

/*

https://leetcode.com/discuss/interview-question/391195/google-onsite-go-game
1. Here given the new out of bound error

2. Given a new black stone to put on empty spot
 */

// For this problem use BFS would be for good
/*
The graph here is
1  1  1   1
1  1  1   1
1  0  0   1
1  1  1   1
 */
var w = 'w'
var b = 'b'
var e = 'e'
var goBoard = arrayOf(charArrayOf(w, b, b, b, b, b, b),
                    charArrayOf(w, b, b, w,  w, w, b),
                     charArrayOf(b, e, b, b, b, b, b),
                    charArrayOf(e, e, e, e, e, e, e))

/*
Output: 1
Explanation: If you place a black stone on
(2, 5) then you capture 1 white stone from the enemy.
 */
val directions = arrayOf(intArrayOf(1, 0), intArrayOf(0, 1), intArrayOf(-1, 0), intArrayOf(0, -1))


// r and c where you palce the stone
fun solveGo(board: Array<CharArray>, r: Int, c:Int):Int{


    var (r , c, count) = listOf(2, 5, 0)


    var visited = Array(goBoard.size) { BooleanArray(goBoard[0].size) }
    var q = LinkedList<IntArray>()
//    q.add(intArray)

    directions.forEach {
        q.add(intArrayOf(r + it[0], c + it[1]))
    }
    while(!q.isEmpty()){

        var (x, y) = q.pop()

        print(goBoard[x][y])
        if(!isInBoundsChar(goBoard,x, y) || visited[x][y] || goBoard[x][y] == 'b' || goBoard[x][y] == 'e'){
            continue

        }else{
            if(goBoard[x][y] == 'w'){
                visited[x][y] = true
                count++

                directions.forEach{
                    q.add(intArrayOf(x + it[0], y+it[1]))
                }
            }
        }
    }

    return count
}
fun isOutOfBounds( board: Array<CharArray>, x: Int, y:Int): Boolean {
    return (x< 0|| y< 0 || x> board.size - 1|| y> board[0].size -1)
}

fun main() {
    /*
    Output: 1
    Explanation: If you place a black stone on
    (2, 5) then you capture 1 white stone from the enemy.
     */
    println(solveGo(goBoard, 2, 5))
}