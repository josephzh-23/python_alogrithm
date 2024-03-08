package String_manipulation

import java.util.*

// O(nlogn) for sort + O(n)

internal class Solution {
    // TC = O(no-word Log(no-word))
    fun arrangeWords(text: String): String {
        val word = text.split(" ".toRegex()).dropLastWhile { it.isEmpty() }.toTypedArray()
        Arrays.sort(word) { s1, s2 -> Integer.compare(s1.length, s2.length) }
        val sen = StringBuilder()
        sen.append(word[0].substring(0, 1).uppercase(Locale.getDefault()) + word[0].substring(1))
        for (i in 1 until word.size) {
            sen.append(" " + word[i].lowercase(Locale.getDefault()))
        }
        return sen.toString().trim { it <= ' ' }
    }
}