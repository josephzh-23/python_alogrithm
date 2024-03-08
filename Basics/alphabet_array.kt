package Basics

import String.MAX_CHAR

fun removeChars(arr: CharArray, k: Int) {
    // Hash table initialised to 0
    val hash = IntArray(MAX_CHAR)
    for (i in 0 until MAX_CHAR) hash[i] = 0

    // Increment the frequency of the character
    val n = arr.size

    // Below is the character
    for (i in 0 until n) {
        val char = arr[i]
        hash[char.toInt() - 'a'.toInt()]++
    }
}