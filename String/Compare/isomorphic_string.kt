package String.Easy

// this is basically where we have 2 words we want to see if
// 1 word can be replaced by the other here

/*
This has the trick right here
 */

fun isIsomorphic(s: String, t: String): Boolean {/*
     Create a mapping between the letter of each word
     s -> a
     */

    // the above would be the 2 difference here
    var mapST = mutableMapOf<Char, Char>()
    var mapTS = mutableMapOf<Char, Char>()
    for (i in 0..s.length) {
        var (c1, c2) = Pair(s[i], t[i])
        if (c1 in mapST && mapST[c1] != c2 || c2 in mapTS && mapTS[c2] != c1) {
            return false
        }
        mapST[c1] = c2
        mapTS[c2] = c1
    }
    return true
}