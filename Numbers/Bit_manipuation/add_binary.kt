fun main() {
    var a = "11"
    var b = "1"
    addBinary(a, b)
}

fun addBinary(a: String, b: String): String {

    var sb = StringBuilder()
    var i = a.length - 1
    var j = b.length - 1

    var carry = 0

    while (i >= 0 && j >= 0) {
        var sum = carry
        if (i >= 0) sum += a[i] - '0'
        if (j >= 0) sum += a[i] - '0'


        // if 1+ 1 = 2 2 %2 = 0 just add 0 then here
        sb.append(sum % 2)
        carry = sum / 2

        i--
        j--

    }

    if (carry != 0) sb.append(carry)
    return sb.reverse().toString()

}