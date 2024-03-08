

/*
Input: dictionary = ["cat","bat","rat"],
sentence = "the cattle was rattled by the battery"

Output: "the cat was rat by the bat"
 */
fun main() {
    var l = listOf("cat", "bat", "rat")
    val sentence = "the cattle was rattled by the battery"
    println(replaceWords(l, sentence))
}


fun replaceWords(roots: List<String>, sentence: String): String {
    val trie = TrieNode()
    for (root in roots) {
        var cur = trie

        /*
In other words this trie here is sort of like the dummy node
it will have 3 paths
" c -  a  -  t"   with word "cat"
* -   " b -  a  -  t"   with word "bat"
" r  - a  -  t"
*/
        // All the roots will be in there
        for (letter in root.toCharArray()) {
            if (cur.children[letter.toInt() - 'a'.toInt()] == null) cur.children[letter.toInt() - 'a'.toInt()] =
                TrieNode()
            cur = cur.children[letter.toInt() - 'a'.toInt()]!!
        }
        cur.word = root
    }
    val ans = StringBuilder()
    for (word in sentence.split("\\s+".toRegex()).dropLastWhile { it.isEmpty() }.toTypedArray()) {
        if (ans.length > 0) ans.append(" ")
        var cur = trie
        for (letter in word.toCharArray()) {
            if (cur.children[letter.toInt() - 'a'.toInt()] == null || cur.word != null) break
            cur = cur.children[letter.toInt() - 'a'.toInt()]!!
        }
        /*
        Basically when cur gets to TrieNode() with "cat"
        the word will be "cat" which is why we return cat here
         */
        ans.append(if (cur.word != null) cur.word else word)
    }
    return ans.toString()
}

internal class TrieNode {
    var children: Array<TrieNode?>
    var word: String? = null

    init {
        children = arrayOfNulls(26)
    }
}