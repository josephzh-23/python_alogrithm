package Recursion


internal class TrieNode {

    // basically each child will be a node
    // j ->   Trienode
    var children: MutableMap<Char, TrieNode> = HashMap()

    // Let you know if at this point there is a word associated here
    // this is a property on the node

    // j->    could have "joseph" for example
    var isWord = false
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
        var curNode: TrieNode? = root
        val arr = word.toCharArray()
        for (curChar in arr) {
            if (curNode!!.children.containsKey(curChar) == false) {
                curNode.children[curChar] = TrieNode()
            }
            curNode = curNode.children[curChar]
        }
        curNode!!.isWord = true
    }

    /** Returns if the word is in the trie.  */
    fun search(word: String): Boolean {
        var curNode: TrieNode? = root
        val arr = word.toCharArray()
        for (curChar in arr) {
            if (curNode!!.children.containsKey(curChar) == false) {
                return false
            }
            curNode = curNode.children[curChar]
        }
        return curNode!!.isWord
    }

    /** Returns if there is any word in the trie that starts with the given prefix.  */
    fun startsWith(prefix: String): Boolean {
        var curNode: TrieNode? = root
        val arr = prefix.toCharArray()
        for (curChar in arr) {
            if (curNode!!.children.containsKey(curChar) == false) {
                return false
            }
            curNode = curNode.children[curChar]
        }
        return true
    }
}

fun main() {
    var s = Tries()
    s.insert("joseph")
    println(s.search("josep"))
}