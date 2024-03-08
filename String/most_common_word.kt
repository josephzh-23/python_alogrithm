
import java.util.*

//O (N+ m)
// O (n + m)

internal class Solution14 {
    fun mostCommonWord(paragraph: String, banned: Array<String?>): String? {

        // 1). replace the punctuations with spaces,
        // and put all letters in lower case
        val normalizedStr = paragraph.replace("[^a-zA-Z0-9 ]".toRegex(), " ").lowercase(Locale.getDefault())

        // 2). split the string into words
        val words = normalizedStr.split("\\s+".toRegex()).dropLastWhile { it.isEmpty() }.toTypedArray()
        val bannedWords: MutableSet<String?> = HashSet<String?>()
        for (word in banned) bannedWords.add(word)
        val wordCount: MutableMap<String?, Int?> = HashMap<String?, Int?>()
        // 3). count the appearance of each word, excluding the banned words
        for (word in words) {
            if (!bannedWords.contains(word)) wordCount[word] = wordCount.getOrDefault(word, 0)!! + 1
        }

        // 4). return the word with the highest frequency
//        return Collections.max<Map.Entry<String?, Int?>>(wordCount.entries, java.util.Map.Entry.comparingByValue()).key

    return ""
    }
}