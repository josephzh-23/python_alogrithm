import Util.printList
import java.util.*

fun main() {
    val num1 = "123"
    val num2 = "456"
    multiply(num1, num2)
}

fun multiply(num1: String, num2: String): String {
    val chs1 = num1.toCharArray()
    val chs2 = num2.toCharArray()
    val n1 = chs1.size
    val n2 = chs2.size
    val res = CharArray(n1 + n2)
    Arrays.fill(res, '0')
    // Start from the back here
    for (j in n2 - 1 downTo 0) {
        for (i in n1 - 1 downTo 0) {

            val digit1 = chs1[i].toInt() - '0'.toInt()
            val digit2 = chs2[j].toInt() - '0'.toInt()
            val product = digit1 * digit2

            // res stores the previous result as well here
            // Adding the previous value into this product as well
            val tmp = res[i + j + 1].toInt() - '0'.toInt() + product
            println("temp is $tmp")
            val remainder = tmp % 10

            // So basically it would be
            res[i + j + 1] = (remainder + '0'.toInt()).toChar()

            val carry = tmp / 10

            //The digit in the front would get the carry
            res[i + j] = (res[i + j].toInt() - '0'.toInt() + carry + '0'.toInt()).toChar()
        }
    }

    printList(res.toList())
    val sb = StringBuilder()
    var seenFirstZero = false
    for (c in res) {

        // false -> true ?
        if (c == '0' && !seenFirstZero) continue
        sb.append(c)
        seenFirstZero = true
    }
    println("result is $sb")
    return if (sb.length == 0) "0" else sb.toString()
}