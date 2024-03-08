//package String
//
//
//
//import kotlin.collections.*
//import kotlin.io.*
//import kotlin.text.*
//
//
///*
// * Complete the 'countNumWays' function below.
// *
// * The function is expected to return an INTEGER.
// * The function accepts following parameters:
// *  1. STRING s
// *  2. INTEGER k
// */
//
//
//fun countNumWays(s: String, k: Int): Int {
//    // Write your code here
//    var chars = s.toCharArray()
//
//    var results = 0
//    // using a 2 pointer to swap
//    for (i in 0 until chars.size - k + 1) {
//        println("at the time is $i")
//        var original = chars.copyOfRange(i, i + 3)
//
//        var afterSwap = swapChar(original, 0, 2)
//        println("the original ${original.joinToString()} and $afterSwap")
//        if (afterSwap > original.toString()) {
//            results++
//        }
//    }
//    return results
//}
//
//
//fun Sliding_window.Basic.Sliding_window.Graph.Hard.main(args: Array<String>) {
//    var s = "amazon"
//
//    var ac = "zam"
//    var ad = "maz"
//
//    println(ac.compareTo(ad))
////    var k = 3
////    val result = countNumWays(s, k)
////
////    println(result)
//}
//
//fun swapChar(cArray: CharArray, i: Int, j: Int): String {
//
//    // Swap the first one
//    var temp = cArray[i]
//    cArray[i] = cArray[j]
//    cArray[j] = temp
//    return StringBuilder().append(cArray).toString()
//
//}
//
//
//
//
//
//
//
//
