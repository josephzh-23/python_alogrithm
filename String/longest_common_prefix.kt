package String


fun main() {

    var arr = arrayOf("flower", "flow" , "flight")
    longestCommonPrefix(arr)
}
fun longestCommonPrefix(strs: Array<String>): String? {
    if (strs.size == 0) return ""
    var prefix = strs[0]
    for (i in 1 until strs.size)
        while (strs[i].indexOf(prefix) != 0) {
        println(strs[i])
            // flower   flowe   flow    flo
        prefix = prefix.substring(0, prefix.length - 1)
//            println(prefix)
            if (prefix.isEmpty()) return ""
        }
    return prefix
}