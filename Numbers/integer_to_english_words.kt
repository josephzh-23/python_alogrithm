package Numbers

private val THOUSANDS = arrayOf("", "Thousand", "Million", "Billion")

private val LESS_THAN_TWENTY = arrayOf(
    "", "One", "Two", "Three", "Four", "Five",
    "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
    "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
)

private val TENS = arrayOf(
    "", "", "Twenty", "Thirty", "Forty", "Fifty",
    "Sixty", "Seventy", "Eighty", "Ninety"
)

fun main() {
    var num = 123
    print(numToWords(123))
}

fun numToWords(num: Int): String {
    var num = num
    if (num == 0) return "zero"
    var sb = StringBuilder()

    // This index will only incrase
    var index = 0
    while (num > 0) {
        if (num % 1000 > 0) {
            println("num is $num")
            var tmp = StringBuilder()
            convertToString(tmp, num % 1000)
            tmp.append(THOUSANDS[index]).append(" ")
            sb.insert(0, tmp)
        }
        index++

        num /= 1000
    }
    return sb.toString().trim()
}

// This works for anything up to 10000 here
fun convertToString(tmp: StringBuilder, num: Int) {
    if (num == 0) {
        return
    } else if (num < 20) {
        tmp.append(LESS_THAN_TWENTY[num]).append(" ")
        return
    } else if (num < 100) {
        tmp.append(TENS[num / 10]).append(" ")
        convertToString(tmp, num % 10)

        // Between 10, 1000 case here
    } else {
        tmp.append(LESS_THAN_TWENTY[num / 100]).append(" Hundred ")
        convertToString(tmp, num % 100)
    }
}