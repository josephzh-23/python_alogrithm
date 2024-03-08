package Basics

fun main(){

    var s = "I am a good word"
    val map = mutableMapOf<Char, Int>()
    for (c in s.toCharArray()) {
        map[c] = map.getOrDefault(c, 0) + 1
    }
}