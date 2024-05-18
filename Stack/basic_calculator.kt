package Hard

import java.util.*

fun main() {

}

fun calculate(s: String): Int {

    /*
    Operand will get resets after every add or - operation
    imagine 1 + (4 + 5)
    after eval 1 + 9 = 10   cur resets to 0
     */
    var cur = 0
    // Everything in here
    var res = 0
    var sign = 1

    /*
    Each time we see a (
    1. want to store the result calculated so far
    and then the sign as well on the top
    2. Reset the sign to 1 and the res to 0 here

     */
    var stack = Stack<Int>()


    for (i in 0 until s.length) {
        val ch = s[i]
        if (Character.isDigit(ch)) {

            // Forming operand, since it could be more than one digit
            cur = 10 * cur + (ch.code - '0'.code)

            // + sign,
            // we first evaluate the expression to
        // the left and then save this sign for the next evaluation
        } else if (ch == '+' || ch== '-') {

            // Evaluate the expression to the left,
            // with result, sign, operand
            res += sign * cur

            // Save the recently encountered '+' sign
            sign = if(ch == '+') 1 else -1
            // Reset operand
            cur = 0

        } else if (ch == '(') {

            // Push the result calculated sofar and sign on to the stack, for later
            // We push the result first, then sign
            // As if we are starting a new result
            stack.push(res)
            stack.push(sign)

            // Reset operand and result, as if new evaluation begins for the new sub-expression
            sign = 1
            res = 0
        } else if (ch == ')') {

            // Evaluate the expression to the left
            // with result, sign and operand
            res += sign * cur

            /*
             ')' will give us the sign that's saved
             marks end of expression within a set of parenthesis
                  Its result is multiplied with sign on top of stack
             */

            res *= stack.pop()

            // Then add to the next operand on the top.
            // as stack.pop() is the result calculated before this parenthesis
            // (operand on stack) + (sign on stack * (result from parenthesis))
            res += stack.pop()

            // Reset the operand
            cur = 0
        }
    }
    return res + sign * cur
}
