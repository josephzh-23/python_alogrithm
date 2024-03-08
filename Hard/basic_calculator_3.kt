package Hard

import java.util.*


// A basic question is like
fun main() {
    var s = Solution33()
    var s3 = "1+(1+1)"
    s.calculate(s3)
}

/*
Basically as soon as we see a (, call the Graph.Edges_question.dfs function to calculate the number
  1 + ( 1 + 2 * 3) ) + 3
 */
internal class Solution33 {
    lateinit var arr: CharArray
    var index = 0
    fun calculate(s: String): Int {
        arr = s.toCharArray()
        return dfs()
    }

    private fun dfs(): Int {
        val stack = Stack<Int>()
        var operator = '+'

        // Get rid of * and /
        while (index < arr.size) {
            if (arr[index] != ' ') {

                // If a digit here
                if (Character.isDigit(arr[index])) {
                    // build the number
                    val buildNum = StringBuilder()

                    while (index < arr.size && Character.isDigit(arr[index])) {
                        buildNum.append(arr[index])
                        index++
                    }

                    // to get back to the number 223+
                    // becomes 223
                    index--

                    // As soon as we have a operator we come here
                    val curNum = buildNum.toString().toInt()
                    insertElement(stack, curNum, operator)


                }

                // If a ( here
                else if (arr[index] == '(') {

                    // Increase index so no lnoger at (
                    // will be 1 idx after
                    index++
                    val curNum = dfs()
                    // This is kind of like backtracking
                    // since we are returning from above here

                    // Once we hit a close bracket ), it will come here
                    // since returning the Graph.Edges_question.dfs above
                    // Why optor needed here?
                    insertElement(stack, curNum, operator)

                    // If closing here
                } else if (arr[index] == ')') {
                    break

                } else {
                    println(operator)
                    operator = arr[index]
                }
            }
            index++
        }
        var total = 0
        while (!stack.isEmpty()) {
            total += stack.pop()
        }
        return total
    }

    private fun insertElement(stack: Stack<Int>, curNum: Int, operator: Char) {
        var curNum = curNum
        if (operator == '-') {
            curNum *= -1
        } else if (operator == '*') {
            curNum *= stack.pop()
        } else if (operator == '/') {
            curNum = stack.pop() / curNum
        }
        println(stack)
        stack.push(curNum)
    }
}