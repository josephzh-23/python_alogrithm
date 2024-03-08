//package String_manipulation
//
//import java.util.*
//import kotlin.collections.HashMap
//
////
//fun arrangeWords2(text: String): String {
//
//    var dict = HashMap<String, Int>()
//    var sentence = text.split(" ")
//
//    for(word in sentence){
//        for(c in word){
//            dict.put(word, dict.getOrDefault(word, 0)+1 )
//        }
//    }
//
//    var maxH: Queue<String> = PriorityQueue{ n1: String, n2: String-> dict[n1]!! - dict[n2]!!}
//
//    // Using this rearranging the words
//}