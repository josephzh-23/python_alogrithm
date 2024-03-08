package tricks

import Coding_Challenges.count
import java.util.*
import kotlin.collections.HashMap

fun main() {
    // build this part first
    var s  = "joseph"
    val counts: MutableMap<Char, Int> = HashMap()

    for(char in s){
        // This can be simplifed using getOrDefault()
        counts.apply {
            put(char, getOrDefault(char, 0) + 1)
        }
    }

    val maxHeap: Queue<Char> = PriorityQueue { a: Char, b: Char ->
        counts.get(a)!! - counts.get(b)!!
    }

}
