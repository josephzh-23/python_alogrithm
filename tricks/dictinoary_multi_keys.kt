package tricks

import java.util.HashMap

fun main() {
    var squares :MutableMap<Pair<Int, Int>, MutableList<Char>> =
            HashMap<Pair<Int, Int>, MutableList<Char>>()
    var i = 0
    var j = 0
    squares.putIfAbsent(Pair(i,j), ArrayList())

    var cood = squares[Pair(i ,j)]
    cood!!.add('4')
//    squares[intArrayOf(i, j)]!!.add('3')
}