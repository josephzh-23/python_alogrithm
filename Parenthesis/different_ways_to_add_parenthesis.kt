package Parenthesis

import java.util.*
import kotlin.collections.HashSet



// https://leetcode.com/problems/different-ways-to-add-parentheses/description/
fun main() {
    var test = "2-1-1"
    var s = Solution15()
    s.diffWaysToCompute(test)
}
internal class Solution15 {
    private val MULTIPLICATION = '*'
    private val ADDITION = '+'
    private val SUBTRACTION = '-'
    private lateinit var expressionArr: CharArray
    private var expression: String? = null
    private val operatorSet: MutableSet<Char> = HashSet()
    fun diffWaysToCompute(expression: String): List<Int> {
        this.expression = expression
        operatorSet.add(MULTIPLICATION)
        operatorSet.add(ADDITION)
        operatorSet.add(SUBTRACTION)
        expressionArr = expression.toCharArray()
        return dfs(0, expressionArr.size - 1)
    }

    private fun dfs(start: Int, end: Int): List<Int> {
        val res: MutableList<Int> = LinkedList()
        for (i in start until end) {

            // This is the case with the "+" and "-"
            // So we need to split here if anything
            /*
            "2-1-1"
            Always add the parenthesis either to the left or the right here
        ((2-1)-1) = 0       to the left
        (2-(1-1)) = 2       to the right
             */
            if (operatorSet.contains(expressionArr[i])) {
                // Give the sum on the left and the right here
                val leftList = dfs(start, i - 1)
                val rightList = dfs(i + 1, end)
                for (num1 in leftList) {
                    for (num2 in rightList) {
                        val totalVal = calculate(num1, num2, expressionArr[i])
                        res.add(totalVal)
                    }
                }
            }
        }
        println(res)
        // The case where we have "23" and then no operator, just
        // add directly here
        if (res.size == 0) {
            res.add(expression!!.substring(start, end + 1).toInt())
        }
        return res
    }

    private fun calculate(num1: Int, num2: Int, operator: Char): Int {
        return when (operator) {
            MULTIPLICATION -> num1 * num2
            ADDITION -> num1 + num2
            SUBTRACTION -> num1 - num2
            else -> -1
        }
    }
}