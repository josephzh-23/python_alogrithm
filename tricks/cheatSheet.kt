package tricks

import java.util.*


fun main() {

    var arr = ArrayList<Int>()

    val n = 0
    val board = Array(n) { CharArray(n) }
    for (cs in board) {
        Arrays.fill(cs, '.')
    }
    var dictWithSet:MutableMap<Int, MutableSet<Int>> = HashMap<Int,MutableSet<Int>>()
    val hash_Set: MutableSet<String> = HashSet()

    var map:MutableMap<Int, Char> = HashMap<Int, Char>()
    // Some trick array function the cheatsheet here
//    Arrays.equals(array1, array2)

    // Using putIfAbsent here

}
