package Basics


fun main() {
    var string1 = "abc"
    val s1map = IntArray(26)

    for(i in 0 until string1.length){
        var char = string1[i]
        s1map[char.code - 'a'.code] = i
    }
    s1map.forEach{
        println(it)
    }

}

fun matches(s1map: IntArray, s2map: IntArray): Boolean {
    for (i in 0..25) {
        if (s1map[i] != s2map[i]) return false
    }
    return true
}