//// Store the last index of each digit here
//// 6  9   9   4
//// 0      2   3
///*
//You are given an integer num. You can swap two digits
//at most once to get the maximum valued number.
//
//Return the max value you can get here
// */
////   then store the last index of the digits here
//fun maxSwap(num: Int): String {
//
//    var numChars = num.toString().toCharArray()
//    var lastIndex = IntArray(10)
//
//    // Store last index of each letter
//    for (i in 0 until numChars.size) {
//        lastIndex[numChars[i] - '0'] = i
//    }
//
//    // 0 ... 9
//    for (i in 0 until numChars.size) {
//        var d = 9
//        while (d > numChars[i] - '0') {
//            println(lastIndex[d])
//            if (lastIndex[d] > i) {
//                var ans = swap2(numChars, lastIndex[d], i)
//                println(ans.toCharArray())
//                return ans.toCharArray().toString()
//            }
//            d--
//        }
//    }
//    return numChars.toString()
//}
//
//fun swap2(str: CharArray, i: Int, j: Int): String {
//    val ch = str
//    val temp = ch[i]
//    ch[i] = ch[j]
//    ch[j] = temp
//    for(c in ch){
//        println(c)
//    }
//    return ch.toString()
//}
//
//fun main() {
//    var rr = 1234
//    println(maxSwap(rr))
//}