package String.Match

// word pattern leetcode

/*
"abba"  ->

"a" -> "dog"
"b" -> "cat"

 */

fun main() {
    var map = mutableMapOf<Char, String>()
    var alphabets = "abba"
    var words = "dog cat cat fish"

    var strings = words.split(" ")
    for(i in 0..alphabets.length -1){
        var char = alphabets[i]

        if(map[char]== null) {
            map[char] = strings[i]
        }else{
            // The case already defined here
            // So we have the code  "ab" "dog cat cat"
            if(map[char] != strings[i]){
                println(false)
            }
        }
    }
    println(true)
}