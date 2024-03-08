import January_3rd.print

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