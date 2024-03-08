package String_manipulation

import java.util.*
import kotlin.collections.HashMap
// Rearrange the letter based on the length here
//https://leetcode.com/problems/rearrange-words-in-a-sentence/
// Problem: rearrange words in a sentence
// brute force approach using q


// 3 a 3b and 2 cs here create the frequency mark here
// Create a set that would store all frequency in the set
// c -> 2   a -> 3  b->3

/*

Count the # of time each word occurs in the whole sentence per char
{c: 3}  means c is in 3 words here
 */
// Use 1 more structure here
// O(m *n)
fun arrangeWords(text: String): String {

    // <Word, count>
    var dict = HashMap<String, Int>()
    var words = text.split(" ")
    words.forEach { word ->
        for (ch in word) {
            dict.put(word, dict.getOrDefault(word, 0) + 1)
        }
    }

    // Based on the string values here
    var maxH: Queue<String> = PriorityQueue { n1: String, n2: String -> dict[n1]!! - dict[n2]!! }
    var s = StringBuilder()
    for (n in dict.keys) {
        maxH.add(n)
    }

    while (!maxH.isEmpty()) {
        s.append(maxH.poll() + " ")

    }

    return s.toString().also { println(it) }

}

fun main() {
    arrangeWords("Leetcode is cool")
    arrangeWords("")
}

