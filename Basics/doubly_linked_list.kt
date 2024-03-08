package Util

import java.util.*
import java.util.ArrayDeque

fun main() {
    // can be used as a stack or a queue as said
    val q: Deque<Int> = ArrayDeque()
    q.removeFirst()
    q.removeLast()

}
