package Parenthesis

import java.util.*


/*
1. See an open, put it on stack, process for later here

2. If we encounter a closing bracket, then we check the element on top of the stack.
If the element at the top of the stack is an opening bracket of the same type,
then we pop it off the stack and continue processing. Else, this implies an
 invalid expression.

3.In the end, if we are left with a stack still having elements,
then this implies an invalid expression.
*/

internal class Solution {
    // Hash table that takes care of the mappings.
    private val mappings: HashMap<Char, Char>

    // Initialize hash map with mappings. This simply makes the code easier to read.
    init {
        mappings = HashMap()
        mappings[')'] = '('
        mappings['}'] = '{'
        mappings[']'] = '['
    }

    fun isValid(s: String): Boolean {

        // Initialize a stack to be used in the algorithm.
        val stack = Stack<Char>()
        for (i in 0 until s.length) {
            val c = s[i]

            // case 1
            // If the current character is a closing bracket.

            // )  a closing bracket here
            if (mappings.containsKey(c)) {

                // Get the top element of the stack. If the stack is empty, set a dummy value of '#'
                val topElement = if (stack.empty()) '#' else stack.pop()

                // If the mapping for this bracket doesn't match the stack's top element, return false.
                // )  ( is not ok then here
                if (topElement != mappings[c]) {
                    return false
                }
            } else {
                // If it was an opening bracket, push to the stack.
                stack.push(c)
            }
        }

        // If the stack still contains elements, then it is an invalid expression.
        return stack.isEmpty()
    }
}