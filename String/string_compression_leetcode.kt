package String


/*
Can only use constant extra space here

String compression problem here it's very easy basically

1. Figure out how many letters you have first each time
2. For each one add the character and then the count
 */
fun main() {
    var charArray = charArrayOf('a', 'a', 'b', 'b', 'c', 'c', 'c')
    compress(charArray)
}
fun compress(chars: CharArray): Int {
    var i = 0
    var resultLength = 0
    while (i < chars.size) {

        // Group len for ("a, "a") is 2, groupLength will keep getting bigger here
        var groupLength = 1

        while (i + groupLength < chars.size && chars[i + groupLength] == chars[i]) {

            groupLength++
            println("length is $groupLength")
        }


        chars[resultLength++] = chars[i]
        if (groupLength > 1) {
            for (c in groupLength.toString()) {
//                println("this is " + Integer.toString(groupLength).toCharArray())
                chars[resultLength++] = c
            }
        }

        // If first one is 2, you skip ahead by 2
        i += groupLength
    }
    println(resultLength)
    return resultLength
}