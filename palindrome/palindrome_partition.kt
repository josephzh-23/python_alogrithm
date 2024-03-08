package palindrome


// Palidnrome partition problem leetcode


// this is the result here this is the 2 lists here
var res = mutableListOf<MutableList<String>>()
fun main() {

    print(partition("aab"))
}

fun partition(str: String): ArrayList<Int> {
    var res = ArrayList<Int>()
    dfs(str, 0, ArrayList())
    return res

}

fun dfs(s: String, start: Int, list: MutableList<String>) {
    if (s.length == start) {
        res.add(ArrayList(list))
        return
    }

    for (i in start until s.length) {

        /*
        Start index will be 0, 1, 2 and then 1, 0, 2 and then sth else here and there

         */
        println("start index is $start and $i")
        /*
         */
        if (isPalindrome(s, start, i)) {
            list.add(s.substring(start, i + 1))
            dfs(s, i + 1, list)
            list.removeAt(list.size - 1)
        }
    }


}

private fun isPalindrome(s: String, start: Int, end: Int): Boolean {
    var start = start
    var end = end
    while (start < end) {
        if (s[start] != s[end]) {
            return false
        }
        start++
        end--
    }
    return true
}
