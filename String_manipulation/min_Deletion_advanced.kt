//package String_manipulation
//
////https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/
//
//// Return the string with the deleted characters
////
//fun minDeletionsAdvanced(s: String): Int {
//    var deletion = 0
//
//    var dict = HashMap<Int, Char>()
//    // Used to store frequency of each character
//    // a-> 3    b-> 2    c-> 2
//    val freq = IntArray(26)
//    for (c in s.toCharArray()) {
//        freq[c - 'a']++
//    }
//    // 3   2   1
//    val uniqueFreq: MutableSet<Int> = HashSet()
//
//    // 3 3
//    // 3 3 3 3
//    for (count in freq) {
//        println(count)
//        var tempCount = 0
//        // if it contains 3, and we see another 3
//        while (count > 0 && uniqueFreq.contains(count)) {
//            deletion++
//            tempCount = count -1
//            resString.append(freq[count])
//        }
//        uniqueFreq.add(tempCount)
//    }
//    return deletion
//}
//
//fun Backtracking.Tree.Hard.Graph.Edges_question.Sliding_window.maining_window.Sliding_window.Graph.Hard.main() {
//    minDeletionsAdvanced("aaabbbcc")
//}
