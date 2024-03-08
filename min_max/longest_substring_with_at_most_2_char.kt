package min_max//package String.Sliding_window
//
//import java.util.*
//import kotlin.collections.HashMap
//
////https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
//
///*
//1. when reach 3 most char
//2. Delete left most index value
//3. Update the left
// */
//
//fun longestSubstringTwoMostCharacters(s: String):Int{
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
//
//fun Sliding_window.Basic.Sliding_window.Graph.Hard.main() {
//    longestSubstringTwoMostCharacters("eceba")
//}