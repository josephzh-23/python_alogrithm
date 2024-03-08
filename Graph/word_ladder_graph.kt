package Hard

import java.util.*

fun ladderLength(beginWord: String, endWord: String, wordList: List<String>?): Int {

    // This is just to store the word list here
    val set: Set<String> = HashSet(wordList)
    if (!set.contains(endWord)) return 0

    val queue: Queue<String> = LinkedList()
    queue.add(beginWord)
    val visited: MutableSet<String> = HashSet()
    visited.add(beginWord)

    var changes = 1
    while (!queue.isEmpty()) {
        val size = queue.size

        // THis tells you how many changes took to get to endword
        // from beginword
        for (i in 0 until size) {
            val words = queue.poll()

            if (words == endWord) return changes

            for (j in 0 until words.length) {
                var k = 'a'.code
                while (k <= 'z'.code) {
                    val arr = words.toCharArray()

                    arr[j] = k.toChar()
                    val str = arr.toString()

                    // Then we have found the string we are looking for
                    // in the string as per example in the notes
                    if (set.contains(str) && !visited.contains(str)) {
                        queue.add(str)
                        visited.add(str)
                    }
                    k++
                }
            }
        }
        ++changes
    }
    return changes
}

fun main() {
    var words = listOf("hot", "dot", "dog", "lot", "log", "cog")
    var beginWord = "hit"
    var endWord = "cog"
    println(ladderLength(beginWord, endWord, words))
}







