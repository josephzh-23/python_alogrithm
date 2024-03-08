package String

/*
We go from the back of the string here
 */
// We then go from the back here

fun main() {
    var num1 = "11"
    var num2 = "233"
    addString(num1, num2)
}

fun addString(num1: String, num2: String) {
    var res = StringBuilder()
    var i = num1.length - 1
    var j = num2.length - 1

    var carry = 0
    while (i >= 0 || j >= 0) {
        var sum = carry

        if (i >= 0) {
            sum += num1[i] - '0'
            i--
        }

        if (j >= 0) {
            sum += num2[j] - '0'
            j--
        }

        res.append(sum % 10)
        carry = sum / 10

        println("carry is $carry")
    }

    if (carry != 0) {
        res.append(carry)
    }

    print(res.reverse().toString())
}