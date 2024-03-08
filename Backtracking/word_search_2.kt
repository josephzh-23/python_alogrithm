package Backtracking

import java.util.*


internal class Solution133 {
    internal inner class TrieNode {
        // This contains all the children here
        var map: MutableMap<Char, TrieNode> = HashMap()
        var isWord = false
    }

    // This would be what we can work with
    var trie = TrieNode()
    var res: MutableList<String> = LinkedList()
    var m = 0
    var n = 0
    lateinit var board: Array<CharArray>
    lateinit var visited: Array<BooleanArray>
    fun findWords(board: Array<CharArray>, words: Array<String>): List<String> {
        //Insert words onto the trie
        for (word in words) {
            insertAWord(word)
        }
        //For each character in board contains in trie, we Graph.Edges_question.dfs
        m = board.size
        n = board[0].size
        this.board = board
        for (row in 0 until m) {
            for (col in 0 until n) {
                val curChar = board[row][col]
                visited = Array(m) { BooleanArray(n) }
                dfs(row, col, StringBuilder(), trie)
            }
        }
        return res
    }

    private fun dfs(row: Int, col: Int, sb: StringBuilder, curTrie: TrieNode?) {
        //Base case
        var curTrie = curTrie
        if (row < 0 || row == m || col == n || col < 0) return
        //Check if visited
        if (visited[row][col]) return

        //Check if current character is in the trie
        val curChar = board[row][col]
        if (!curTrie!!.map.containsKey(curChar)) return
        sb.append(curChar)

        // Get you the trie based on the char 'j', 'i', or what not
        curTrie = curTrie.map[curChar]
        visited[row][col] = true
        //Add current string to the res if it is a word
        if (curTrie!!.isWord) {
            res.add(sb.toString())
            curTrie.isWord = false
        }

        //DFS all 4 directions
        dfs(row, col + 1, sb, curTrie) //right
        dfs(row + 1, col, sb, curTrie) //Down
        dfs(row - 1, col, sb, curTrie) //Up
        dfs(row, col - 1, sb, curTrie) //left
        //Remove last element: Backtracking
        // Why do we have to remove things here?

        // We have to back track for example
        // hfkl and hkl  here look at what we can do here

        sb.setLength(sb.length - 1)
        visited[row][col] = false
    }

    private fun insertAWord(word: String) {
        val arr = word.toCharArray()
        var curNode: TrieNode? = trie
        for (curChar in arr) {
            if (!curNode!!.map.containsKey(curChar)) {
                curNode.map[curChar] = TrieNode()
            }
            curNode = curNode.map[curChar]
        }
        curNode!!.isWord = true
    }
}