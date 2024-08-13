import java.util.*


// This is actually a bfs solution here
/*

 s = "applepenapple",
  wordDict = ["apple","pen"]
so the word s can be separated here
 */

fun main() {
    var word = "leetcode"
    var wordDict= listOf("leet", "code")
    wordBreak(word, wordDict)
}
    // from a node start we can move to end if
    // substrig s between start, end exists in wordDict

fun wordBreak(s: String, wordDict: List<String>?): Boolean {

   // Uique qoreds
    val words: Set<String> = HashSet(wordDict)
    val queue: Queue<Int> = LinkedList()

    // Store the index of the array seen
    val seen = BooleanArray(s.length + 1)
    queue.add(0)
    while (!queue.isEmpty()) {
        /*
Using exmample baove, the first time it comes here the
start will then be 4 the next time is 8
         */
        val start = queue.remove()
        println("start is $start")
        if (start == s.length) {
            return true
        }


        for (end in start + 1..s.length) {
            if (seen[end]) {
                continue
            }
            // say the word is
            if (words.contains(s.substring(start, end))) {
                queue.add(end)
                seen[end] = true
            }
        }
    }
    return false
}