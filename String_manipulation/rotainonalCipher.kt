import January_3rd.print


'''
The problem is basiccally here where if you rotate zebra-493 by 3 places here? and then what happens is that

Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?"



here everything is rotated 3 characters higher interseing problem here


'''
fun rotationalCipher(input: String, rotationFactor: Int): String? {
    val ordA = 'A'
    val orda = 'a'
    val output = StringBuilder()


    for (ch in input.toCharArray()) {
        if (Character.isDigit(ch)) {
            output.append((ch.hashCode() + rotationFactor) % 10)

        } else if (Character.isAlphabetic(ch.toInt())) {
            if (Character.isUpperCase(ch)) {
                val temp = (ch - ordA + rotationFactor) % 26
                output.append((ordA + temp))
            } else {
                val temp = (ch - orda + rotationFactor) % 26
                output.append((orda + temp))
            }
        } else {
            output.append(ch)
        }
    }
    return output.toString()
}

fun main() {
    var (input, factor) = Pair("Zebra-493?",3 )
    rotationalCipher(input, factor).print()
}