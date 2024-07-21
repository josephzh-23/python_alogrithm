package String.Match


/*
Example:
['world', 'word', 'would', 'wont', 'which', 'hello']
'w3*d'
 */


# using the 2 pointer technique here
fun match(words: Array<String>, abbr: String): List<String> {
    val res: MutableList<String> = ArrayList()
    for (word in words) {
        if (isValid(word, abbr)) {
            res.add(word)
            print(word)
        }
    }
    return res
}

fun isValid(word: String, abbr: String): Boolean {
    var i = 0
    var j = 0
    while (i < word.length && j < abbr.length) {
        if (Character.isDigit(abbr[j])) {
            var num = 0


            while (j < abbr.length && Character.isDigit(abbr[j])) {
                num += num * 10 + (abbr[j].toInt() - '0'.toInt())
                j++
            }
            i += num
            j++
        }
        println("j is $j")
        if (i >= word.length) {
            break
        }
        if (word[i] == abbr[j]) {
            i++
            j++
        } else {
            return false
        }
    }
    return i == word.length && j == abbr.length
}


fun main(args: Array<String>) {
//    val input = arrayOf("world", "would", "hello", "word")
    val input = arrayOf("world")
    print(match(input, "w3*d").size)
}