package Parenthesis

// Min remove to make valid parenthesis
fun main() {

}


fun minRemoveToMakeValid(s: String): String {
    val ch = s.toCharArray()

    //left to right
    //)---> (
    var count = 0
    for (i in ch.indices) {

        // When you first see ( add
        if (ch[i] == '(') {
            count++
        } else if (ch[i] == ')') {
            if (count > 0) {
                count--

                // The first invalid we have found that do not have a
                // valid parenthesis here
            } else {
                ch[i] = 0.toChar()
            }
        }
    }

    // Below we are repeating from the right ot the left here
    //right->left
    // ( ----> )
    count = 0
    for (i in ch.indices.reversed()) {
        if (ch[i] == ')') {
            count++
        } else if (ch[i] == '(') {
            if (count > 0) {
                count--
            } else {
                ch[i] = 0.toChar()
            }
        }
    }
    val sb = StringBuilder()
    for (c in ch) {

        // If not 0 then that's the one that we wanted to add
        if (c.toInt() != 0) {
            sb.append(c)
        }
    }
    return sb.toString()
}