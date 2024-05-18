package Hard

import January_3rd.print
import java.util.*

fun main() {
    // The calculate number here
    calculate2("3+2*3").print()
}

fun calculate2(s: String?): Int {
    if (s == null || s.isEmpty()) return 0
    val len = s.length
    val stack = Stack<Int>()

    /*
    Keep track of the cur number
    3 + 2 * 3
    2 will be cur Number

    The trick:
    Basically the first time we see *, the sign down below will actually
    still be + so 2 gets pushed into stack as well

     */
    var currentNumber = 0
    var sign = '+'
    for (i in 0 until len) {
        val currentChar = s[i]

        // Multi-digit case
        if (Character.isDigit(currentChar)) {
            currentNumber = currentNumber * 10 + (currentChar.code - '0'.code)
        }

        // If not see a digit
        if (!Character.isDigit(currentChar) && !Character.isWhitespace(currentChar) || i == len - 1) {
            // + - cases push to stack to be popped later
            if (sign == '-') {
//                println("stack is $stack")

                stack.push(-currentNumber)

                /*
        In the example above since 3 + 2 * 3

                 */
            } else if (sign == '+') {


                stack.push(currentNumber)
                println("stack is $stack")

                // * and / cases here
            } else if (sign == '*') {


                var popped = stack.pop()
                println("cur is $popped $currentNumber")

                // Here stack.pop() gives 2 and curNumber
                stack.push(popped * currentNumber)
//                println("stack is $stack")
            } else if (sign == '/') {
                stack.push(stack.pop() / currentNumber)
            }
            sign = currentChar
            currentNumber = 0
        }
    }
    var result = 0
    while (!stack.isEmpty()) {
        result += stack.pop()
    }
    return result
}