package Hard

import java.util.*


/*
https://leetcode.com/problems/longest-string-chain/

Idea here
1. Map<String, Integer> map: the longest chain ends with string

2. use a preLen = the lenght of the previous word

Basically there is a subsequence relationship here
    if (isSubsequence(preWord, word))

2 conditions for the newLength
1. newLength = previousLengh + 1
2.

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
 */




fun longestStrChain(words: Array<String>): Int {
    val dp: MutableMap<String, Int> = HashMap()

    // Sorting the list in terms of the word length.
    Arrays.sort(words) { a: String, b: String -> a.length - b.length }
    var longestWordSequenceLength = 1
    for (word in words) {
        var presentLength = 1

        // Why this?
        /*
        Ex: abcd    has both abd    abc
        abc could already have 3 and abd has 1
        so we go with abc
         */
        // Find all possible predecessors for the current word by removing one letter at a time.
        for (i in 0 until word.length) {
            val temp = StringBuilder(word)
            temp.deleteCharAt(i)
            val predecessor = temp.toString()
            val previousLength = dp.getOrDefault(predecessor, 0)
            presentLength = Math.max(presentLength, previousLength + 1)
        }

        dp[word] = presentLength

        // Update the biggest one so far at each turn
        longestWordSequenceLength = Math.max(longestWordSequenceLength, presentLength)
    }
    return longestWordSequenceLength
}


fun main() {
    var words = arrayOf("ba", "bad")
    appearBefore(words)
}
// check if contains previous word first
fun appearBefore(words: Array<String>) {
    val dp: MutableMap<String, Int> = HashMap()
    var appearBefore = false
    for(word in words){
        var presentLength = 0
        // Check if previous word occurs here
        for(i in 0 until word.length){
            val temp = java.lang.StringBuilder(word)
            val prevWord =  temp.deleteCharAt(i).toString()
            println(prevWord)
            if(dp.getOrDefault(prevWord, 0) > 1){
                appearBefore = true
            }
            //
            presentLength++
        }
        dp[word] = presentLength
    }
    println(appearBefore)

}








