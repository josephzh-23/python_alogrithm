package String_manipulation

import String.MAX_CHAR

fun removeChars(arr: CharArray, k: Int) {
    // Hash table initialised to 0
    val hash = IntArray(MAX_CHAR)
    for (i in 0 until MAX_CHAR) hash[i] = 0

    // Increment the frequency of the character
    val n = arr.size

    var arr = StringBuilder()

    // Below is the character
    for (i in 0 until n) {
        val char = arr[i]
        hash[char.toInt() - 'a'.toInt()]++
    }

    // Next index in reduced string
    var index = 0
    for (i in 0 until n) {
        val char = arr[i]
        hash[char.toInt() - 'a'.toInt()]++
        if(hash[char.toInt() - 'a'.toInt()] < k){
            arr.append(char)
        }
    }

}