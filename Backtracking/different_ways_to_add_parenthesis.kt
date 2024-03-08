package Backtracking

import java.util.*
import kotlin.collections.HashSet


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
            if (operatorSet.contains(expressionArr[i])) {
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