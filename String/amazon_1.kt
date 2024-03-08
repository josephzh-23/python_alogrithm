package String


import kotlin.collections.*
import kotlin.io.*
import kotlin.text.*


/*
 * Complete the 'countNumWays' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. STRING s
 *  2. INTEGER k
 */


fun countNumWays(s: String, k: Int): Int {
    // Write your code here
    var chars = s.toCharArray()

    var results = 0
    // using a 2 pointer to swap
    for (i in 0 until chars.size - k + 1) {
        println("at the time is $i")
        var original = chars.copyOfRange(i, i + k)

        var afterSwap = swapChar2(original, 0, k-1)
        var originalString = StringBuilder().append(original).toString().reversed()
        if (afterSwap < originalString) {
            results++
        }
    }
    return results
}


fun main(args: Array<String>) {
   var s = "ababa"

    var ac = "abd"
    var ad = "abc"

//    println(ac.compareTo(ad))
    var k = 2
    val result = countNumWays(s, k)

    println(result)
}

fun swapChar2(cArray: CharArray, i: Int, j: Int): String {

    // Swap the first one
    var temp = cArray[i]
    cArray[i] = cArray[j]
    cArray[j] = temp
    return StringBuilder().append(cArray).toString()

}








