package tricks


fun main() {
    var s = "123"

    calculate(s)
}
fun calculate(s: String):Int{
    var operand = 0
    for (i in 0 until s.length) {
        val ch = s[i]
        if (Character.isDigit(ch)) {
            println(operand)
            // Forming operand, since it could be more than one digit
            operand = 10 * operand + (ch.code - '0'.code)
        }
    }
    return operand
}