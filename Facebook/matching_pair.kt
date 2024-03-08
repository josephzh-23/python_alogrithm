package Facebook



// Each charcater has at least k frequencies
/*
1. If we found a pair like
        s-{a,b}, t-{b, a}   swapping increase match by 2

2. If we found
    s- {a, t}, t- {t, b}    swapping increase match by 1

3. If any repeating char
    s-{a, b} , t- {c, d}    swapping will not increase

4. Reduce the final answer by 2 so far
 */

fun matchingPairs(s: String, t: String): Int {
    val mismatchS: MutableSet<String> = HashSet()
    val sToChar = s.toCharArray()
    val tToChar = t.toCharArray()
    var matching = 0
    for (i in sToChar.indices) {
        if (sToChar[i] != tToChar[i]) {
            mismatchS.add(sToChar[i].toString() + "" + tToChar[i])
        } else matching++
    }
    for (mism in mismatchS) {
        val reverse = mism[1].toString() + "" + mism[0]
        if (mismatchS.contains(reverse)) {
            return matching + 2
        }
    }
    if (mismatchS.size <= 1) matching--
    if (mismatchS.size == 0) matching--
    return matching
}










