package Util

fun frequencyOfCharacters(s: String) {
    var deletion = 0
    var map= mutableMapOf<Char, Int>()


    // another way to store
    for (c in s.toCharArray()) {
        map[c] = map.getOrDefault(c, 0) + 1
    }

    // Used to store frequency of each character
    // a-> 3    b-> 2    c-> 2
    val freq = IntArray(26)
    for (c in s.toCharArray()) {
        freq[c - 'a']++
    }
    map
}
fun main() {
    frequencyOfCharacters("joeeee")
}