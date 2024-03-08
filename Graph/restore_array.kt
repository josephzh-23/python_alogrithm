fun main() {
    val add =arrayOf(intArrayOf(4, -2), intArrayOf(1, 4), intArrayOf(-3, 1)
    )

    restoreArray(add).forEach{
        println(it)
    }
}

fun restoreArray(ap: Array<IntArray>): IntArray {
    val hm = HashMap<Int, MutableList<Int>>()
    val n = ap.size
    for (i in ap.indices) {
        hm.putIfAbsent(ap[i][0], ArrayList())
        hm[ap[i][0]]!!.add(ap[i][1])
        hm.putIfAbsent(ap[i][1], ArrayList())
        hm[ap[i][1]]!!.add(ap[i][0])
    }
    var start = 0

    // Once you get the start here hten you can add htis in the next one as
    // discussed
    for ((key, value) in hm) {
        if (value.size == 1) {
            start = key
            break
        }
    }
    val ans = IntArray(n+1)
    val seen = HashSet<Int>()
    dfs(hm, start, 0, seen, ans)
    return ans
}

private fun dfs(
    hm: HashMap<Int, MutableList<Int>>, start: Int,
    index: Int, seen: HashSet<Int>, ans: IntArray
) {

    ans[index] = start
    seen.add(start)
    for (neigh in hm[start]!!) {
        if (!seen.contains(neigh)) {
            dfs(hm, neigh, index + 1, seen, ans)
        }
    }
}