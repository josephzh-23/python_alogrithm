package String.Hard


// https://leetcode.com/problems/text-justification/description/
fun main() {


}

fun fullyJustify(words: List<String>, maxWidth: Int) {
    var result = mutableListOf<String>()

    var (i, n) = listOf(0, words.size)

    // How many words each time, i is the number of words
    while (i < n) {
        // 0, 1
        var j = i + 1
        var lineLength = words[i].length // j - i -1 # of spaces between each word here
        while (j < n && lineLength + words[j].length + (j - i - 1) < maxWidth) {
            lineLength += words[j].length
            j++
        } // The
        var spacesAvailable = maxWidth - lineLength
        var numberOfWords = j - i

        /*
        If only 1 word j >= n (if j pointer is on the very last line there)
         */
        if (numberOfWords == 1 || j >= n) result.add(leftJustify(words, spacesAvailable, i, j))
        else result.add(middleJustify(words, spacesAvailable, i, j).toString())
    }

}

fun middleJustify(words: List<String>, spacesAvailable: Int, i: Int, j: Int): StringBuilder {
    var spacesNeeded = j - i - 1
    var spacesInBetween = spacesAvailable / spacesNeeded
    var extraSpaces = spacesAvailable % spacesNeeded

    // Again initialize the res with what's already there
    var res = StringBuilder(words[i])
    for (k in i + 1 until j) {
        extraSpaces--
        var spacesToApply = spacesInBetween + if (extraSpaces > 0) 1 else 0
        res.append(" ".repeat(spacesToApply) + words[k])
    }
    return res
}

// We only have 1 word left on the last line there and j >=n has exceeded here
// Have a bunch of words on the right here
fun leftJustify(words: List<String>, diff: Int, i: Int, j: Int): String {

    // Initialize the string to whatever the current string is
    var res = StringBuilder(words[i])
    var spacesOnTheRight = diff - j - i - 1

    // Add the space to the word
    for (k in i + 1 until j) {
        res.append(" " + words[k])
    }

    res.append(" ".repeat(spacesOnTheRight))
    return res.toString()
}
