package String

import Util.printList
import java.util.*


fun main() {
    var words = arrayOf("i","love","leetcode","i","love","coding")
    topKFrequentWords(words,2)
}
/*
The answer here has to be sorted as well as said
 */
    fun topKFrequentWords(words: Array<String>, k: Int): List<String?>? {
        val map: MutableMap<String, Int> = HashMap()
        for (word in words) {
            map[word] = map.getOrDefault(word, 0) + 1
        }
        val pq = PriorityQueue<String> { word1, word2 ->
            val freq1 = map[word1]!!
            val freq2 = map[word2]!!

            // If their freq the same then compare alphabetically
            if (freq1 == freq2) word2.compareTo(word1) else freq1 - freq2
        }
        map.forEach{
            pq.add(it.key)
            if (pq.size > k) pq.poll()
        }
        val result: MutableList<String?> = ArrayList()

    //Transfer from the pq to the result array
        while (!pq.isEmpty()) result.add(pq.poll())
        result.reverse()
        printList(result)
        return result
    }






