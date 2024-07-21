package Stacks_Queue

import java.util.*

internal class Pair(var cnt: Int, var ch: Char)

fun removeDuplicates(s: String, k: Int): String? {
    val counts: Stack<Pair> = Stack()
    for (i in s.indices) {
        if (counts.empty() || s[i] != counts.peek().ch) {
            counts.push(Pair(1, s[i]))
        } else {
            if (++counts.peek().cnt === k) {
                counts.pop()
            }
        }
    }
    val b = StringBuilder()
    while (!counts.empty()) {
        val p: Pair = counts.pop()
        for (i in 0 until p.cnt) {
            // We push the character up there
            b.append(p.ch)
        }
    }
    return b.reverse().toString()
}