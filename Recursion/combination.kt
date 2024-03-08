// Example n = 4, k = 2
/*
[1, 2]  [1, 3]  [1, 4]  [2, 3]  [2, 4]   [3, 4]
 */
fun combine(n: Int, numElem: Int): List<List<Int>> {
    if (numElem > n) return ArrayList()
    val result: MutableList<List<Int>> = ArrayList()
    combine(1, n, numElem, ArrayList(), result)
    return result
}

// n is the maximum number allowed in there
private fun combine(i: Int, n: Int, numElem: Int, comb: MutableList<Int>, result: MutableList<List<Int>>) {
    if (numElem == 0) {
        result.add(ArrayList(comb))
        return
    }
    for (x in i..n) {
        comb.add(x)
        // backtrack here
        combine(x + 1, n, numElem - 1, comb, result)
        comb.removeAt(comb.size - 1)
    }
}
