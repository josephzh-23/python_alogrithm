package Numbers



fun main() {
    var s = "123"

    print(calculate(s))
}

// Must take care of the sign too
fun calculate(s: String):Int{
    var sb = StringBuilder()
    var negative = false


    var answer = 0

    // Check the answer first

    for (i in 0 until s.length) {


        val ch = s[i]
        if (Character.isDigit(ch)) {
            // Forming operand, since it could be more than one digit
            answer = 10 * answer + (ch.code - '0'.code)
        }
    }
    return answer
}