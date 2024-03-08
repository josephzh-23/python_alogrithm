package Array.two_pointer

/*
Reverse the whole thing first
you are joseph
hpesoj era uoy
then rever each word individually
joseph are you
 */

fun main() {
    var word = "you are joseph"
   reverseWords2(word.toCharArray())
}
// Using 2 pointer approach here
fun reverse(s: CharArray, left: Int, right: Int) {
    var left = left
    var right = right
    while (left < right) {
        val tmp = s[left]
        s[left] = s[right]
        s[right] = tmp
        left++
        right--
    }
}

// The 2nd part of this
fun reverseEachWord(s: CharArray) {
    val n = s.size
    var start = 0

    // Use an end index to track basically and then keep going
    var end = 0
    while (start < n) {

        // go to the end of the word
        while (end < n && s[end] != ' ') ++end
        // reverse the word
        reverse(s, start, end - 1)
        // move to the next word
        start = end + 1
        ++end
    }
}

fun reverseWords2(s: CharArray) {
    // reverse the whole string
    reverse(s, 0, s.size - 1)

    // reverse each word
    reverseEachWord(s)
    println(s)
}