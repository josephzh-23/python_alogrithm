package String.Sliding_window//import java.util.*
//import kotlin.collections.HashMap
//
//// Turns out much more complicated than initially thought possible as said
//// If you can get twice done with the amount of work that you specificed
//
//// and maybe using the code you can evven find something e
//
//// at least k repeating here
//fun String.Sliding_window.longestSubstringTwoMostCharacters(s: String):Int{
//
//    var n = s.length
//    var l = 0 ; var r = 0;
//    // hashmap character -> its rightmost position
//    // in the sliding window
//    val hp = HashMap<Char, Int>()
//
//    var maxLen = 2
//
//    while(r< n){
//        // when the slidewindow contains less than 3 characters
//        // a b c d
//        // a ->0   b-> 1   c-> 2
//        hp.put(s[r], r++)
//
//
//        // Since we will have 2 char at most
//        if(hp.size ==3){
//
//            // Delet the left most character since window
//            // need to be slided now
//            val leftMostIndex = Collections.min(hp.values)
//            //delete this char
//            hp.remove(s[leftMostIndex])
//
//            l = leftMostIndex + 1
//        }
//        maxLen = Math.max(maxLen, r - l)
//    }
//
//    println(maxLen)
//    return maxLen
//
//    return 0
//}
