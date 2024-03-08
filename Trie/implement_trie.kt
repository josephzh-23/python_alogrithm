package Trie

import Recursion.Trie.ALPHABET_SIZE


private class TrieNode {
    var children = arrayOfNulls<TrieNode>(ALPHABET_SIZE)

    // isEndOfWord is true if the node
    // represents end of a word
    var isEndOfWord = false
    var word: String = ""
}
class Tries {

    // this is the curnode
    private val root: TrieNode

    /** Initialize your data structure here.  */
    init {
        root = TrieNode()
    }

    /** Inserts a word into the trie.  */
    fun insert(word: String) {

        // Same as a binary tree
        var curNode: TrieNode? = root
        val arr = word.toCharArray()
        for (curChar in arr) {

            // This would be the index
            val index = curChar- 'a'

            if (curNode!!.children[index] == null) {
                curNode.children[index] = TrieNode()
            }

            // Moving down the chain inside the tree
            curNode = curNode.children[index]
        }
        curNode!!.isEndOfWord = true
    }

    /** Returns if the word is in the trie.  */
    fun search(word: String): Boolean {
        var curNode: TrieNode? = root
        val arr = word.toCharArray()
        for (curChar in arr) {

            val index = curChar- 'a'
            if (curNode!!.children[index] == null) {
                return false
            }
            curNode = curNode.children[index]
        }
        return curNode!!.isEndOfWord
    }

    /** Returns if there is any word in the trie that starts with the given prefix.  */
    fun startsWith(prefix: String): Boolean {
        var curNode: TrieNode? = root
        val arr = prefix.toCharArray()
        for (curChar in arr) {
            val index = curChar- 'a'

            if (curNode!!.children[index] == null) {
                return false
            }
            curNode = curNode.children[index]
        }
        return true
    }
}

fun main() {
    var s = Tries()
    s.insert("joseph")
    println(s.search("josep"))
}