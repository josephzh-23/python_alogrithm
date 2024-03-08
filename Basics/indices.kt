package Util

fun main() {
    var n =4
    var parents =IntArray(n)
    // indices here would give you 0, 1,2, 3 would give the position
    // of character in array or index
    // sort of like range in python
    for (i in parents.indices) {
        parents[i] = i
        println(i)
    }
}
