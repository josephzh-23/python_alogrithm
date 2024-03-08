package Tree

import java.util.HashMap



fun main() {

    var str = arrayOf("abc", "bcd", "acef", "xyz", "az", "ba", "a", "z")

    println(groupStrings(str))
}


fun groupStrings(strings: Array<String>): MutableCollection<MutableList<String>> {
   // More important here
    val result: MutableMap<String, MutableList<String>> = HashMap()

    // This give you the code
    /*
    You can have "abc" -> "bcd" and all that and that's it
     */
    strings.forEach { word ->
        // The key is right here
        var key = ""

        var size = word.length

        for (i in 1 until size) {

            // The following is kind of important as said
            key += (word[i] - word[i - 1] + 26) % 26
            println("the key is $key")
        }

//        println("the key is $key")

        result.computeIfAbsent(key){ArrayList()}.add(word)
    }
    return result.values
}

