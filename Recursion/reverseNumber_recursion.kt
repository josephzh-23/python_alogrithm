package January_3rd
fun main() {
    var s = "123"
    reverseNumber(123)
}

fun reverseNumber(original: Int) {
    var reverseNum = 0
    var tempOriginal = original

    // tempOriginal will be 12, 1, 0
    while (tempOriginal > 0) {
        val lastDigit = tempOriginal % 10
        reverseNum = reverseNum * 10 + lastDigit
        tempOriginal = tempOriginal/ 10

    }

    println(reverseNum)
}
