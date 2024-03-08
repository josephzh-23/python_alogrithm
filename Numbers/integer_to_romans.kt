package Numbers

// So to start off here
fun main() {
    intToRoman(11500)
}


private val values = intArrayOf(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
private val symbols = arrayOf("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
fun intToRoman(num: Int): String {
    var num = num
    var roman = StringBuilder()
    for(i in values.indices){
            while(num >= values[i]){
                roman = roman.append(symbols[i])

                // This needs to decrease here
                num -= values[i]
            }
    }
    return roman.toString()
}