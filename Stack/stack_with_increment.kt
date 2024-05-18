package Stacks_Queue

import java.util.*

class CustomStack(maxSize: Int) {
    var q: Queue<Int> = LinkedList()
    var s= Stack<Int>()
    var size = maxSize
    fun push(x: Int) {
        q.add(x)
        s.add(x)
    }

    fun pop(): Int {
        if(!s.isEmpty()) {
            return s.pop()
        }else{
            return -1
        }
    }

    fun increment(k: Int, `val`: Int) {

    }

}
