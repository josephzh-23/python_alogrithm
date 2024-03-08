package String_manipulation

fun removePunctuation(input: String): String? {
    val builder = StringBuilder()
    for (c in input.toCharArray()) if (Character.isLetterOrDigit(c)) builder.append(if (Character.isLowerCase(c)) c else c.lowercaseChar())
    return builder.toString().also{println(it)}
}

fun main() {
    removePunctuation("joseph####")
}