package Util

fun main() {
    val list = listOf("One", "Two", "Three")

    for (i in list.indices.reversed()) {
        println(list[i])
    }
}