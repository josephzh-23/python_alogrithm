package Trial

import java.util.*

/*
Check if the string scanned so far is valid
find the length of the longest valid string

Start by pushing -1 onto the stack, for
every ( encountered, push unto the stack here

For every ')' encountered, we pop the topmost element. Then,
the curLength = cur element index - top element stack
 */

fun longestValidParentheses(s: String): Int {
    var maxans = 0
    val stack: Stack<Int> = Stack()
    stack.push(-1)
    for (i in 0 until s.length) {
        if (s[i] == '(') {
            stack.push(i)
        } else {
            stack.pop()
            if (stack.empty()) {
                stack.push(i)
            } else {
                maxans = Math.max(maxans, i - stack.peek())
            }
        }
    }
    return maxans
}