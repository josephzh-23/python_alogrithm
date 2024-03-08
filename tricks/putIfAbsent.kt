package tricks

import java.util.HashMap

fun main() {
    var rows:MutableMap<Int, MutableList<Char>> = HashMap<Int,MutableList<Char>>()
    // Using dicitonary with set

    // This is absolutely necessary here otherwise not gonna work here
    rows.putIfAbsent(0, ArrayList())
    rows[0]!!.add('d')
}