import java.util.*


fun main() {
    decodeString("3[a2[c]]")
}

fun decodeString(s: String): String {
    val countStack: Stack<Int> = Stack()
    val stringStack: Stack<StringBuilder> = Stack()
    var currentString = StringBuilder()
    var k = 0
    for (ch in s.toCharArray()) {
        if (Character.isDigit(ch)) {
            k = k * 10 + ch.toInt() - '0'.toInt()
        } else if (ch == '[') {
            // push the number k to countStack

            // Basically in the case here we would have a case where
            // [3[a2[c]]]       -> this would turn into 6 cs then here
            countStack.push(k)

            // This would store everything that comes before the [

            stringStack.push(currentString)
            // reset currentString and k
            currentString = StringBuilder()
            k = 0
        } else if (ch == ']') {
            println("String stack is $stringStack")
            val decodedString: StringBuilder = stringStack.pop()

            println("count stack here is $countStack with $currentString")
            // Make sure this gets counted 4 times if there are 4c in the front
            for (currentK in countStack.pop() downTo 1) {
                decodedString.append(currentString)
            }
            currentString = decodedString

            // The case where it's just the string here
        } else {
            currentString.append(ch)
        }
    }
    println("the end result is $currentString")
    return currentString.toString()
}