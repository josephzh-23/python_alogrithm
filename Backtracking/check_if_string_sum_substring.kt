//package Backtracking
//
//// A given string sum-substring here
//
//package Backtracking
//
//
//import print
//import java.util.*
//
///*
//Using the string return if the following string has
//
//"using backstring"
// */
//
//class restore_ip_addresses2 {
//    var res: MutableList<String> = LinkedList()
//    fun restoreIpAddresses(s: String): List<String> {
//        val n = s.length
//        if (n == 0) {
//            return res
//        }
//        Graph.Edges_question.dfs(StringBuilder(), s)
////        print(res)
//        return res
//    }
//
//    // As there would 4 sections here since we have 4 sections in the ip
//    // addresses
//    // str: the string builder each time
//    /*
//    s: string here would gradually get smaller
//     */
//    private fun Graph.Edges_question.dfs(str: StringBuilder, s: String) {
//        println(s)
//        var str = str
//        val n = s.length
//
//        // We have reached the end and we have found 1 combination here
//
//        if (n == 0 ) {
//            res.add(str.substring(0, str.length - 1).toString())
//            return
//        }
//        val sb = StringBuilder()
//        val min = Math.min(s.length, 3)
//
//        // Up to the length 3
//        for (i in 0 until min) {
//            sb.append(s[i])
//
//            // Convert it to number here
//            val value = sb.toString().toInt()
//            println(sb)
//
//
//            // If valid then try adding the . at the end
//            // Ex: 1 -> 1.
//            val temp = StringBuilder(str)
//            str.append(sb)
//            str.append('.')
//
//            println(str)
//            // And then here is the
//            Graph.Edges_question.dfs(str, s.substring(i + 1, s.length))
//
//            // reset our current string for the next backtracking here
//            str = temp
//        }
//    }
//}
//
//fun Graph.Edges_question.Sliding_window.maining_window.Sliding_window.Graph.Hard.main() {
//    var s = restore_ip_addresses2()
//    s.restoreIpAddresses("1010").print()
//}