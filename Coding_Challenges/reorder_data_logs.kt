package Coding_Challenges

import java.util.*

fun main() {
    var logs = arrayOf(
            "dig1 8 1 5 1",
            "let1 art can",
            "dig2 3 6",
            "let2 own kit dig",
            "let3 art zero"
    )
    var res = reOrderDataLogs(logs)
    res.forEach{
        println(res)
    }
}
    fun reOrderDataLogs(logs: Array<String>): Array<String> {
        Arrays.sort(logs) { log1: String, log2: String ->
            val arr1 = splitStr(log1)
            val arr2 = splitStr(log2)

            // check the first character here if it's number
            val isNum1 = Character.isDigit(arr1[1][0])
            val isNum2 = Character.isDigit(arr2[1][0])

            // then stat the same
//            if(!isNum1 && !isNum2){
//                return
//            }
            // At this point it's all letter logs otherwise returned already
            val isSameContent = arr1[1] == arr2[1]

            // Go back to comparing the first index of each word in here
            if (isSameContent) {
                println("both string logs ")
                return@sort arr1[0].compareTo(arr2[0])
            } else {
                println("both digit logs here")
                // If not the same content
                // In other words "digit logs"
                return@sort arr1[1].compareTo(arr2[1])
            }
        }
        return logs
    }

    private fun splitStr(log: String): Array<String> {
        return log.split(" ".toRegex()).dropLastWhile { it.isEmpty() }.toTypedArray()
    }

    private fun isNumber(curChar: Char): Boolean {
        return '0' <= curChar && curChar <= '9'
    }