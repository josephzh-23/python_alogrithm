package String.substring

/*

For each prefix of lengt i that divides n,
 */

fun main() {
    var s = "abab"
    repeatedSubstringPattern(s)
}
fun repeatedSubstringPattern(s: String): Boolean {
    val n = s.length
    for (i in 1..n / 2) {

        /*
        Using an example here would make sense

         */
        if (n % i == 0) {
            val pattern = StringBuilder()

            /*

    Basically how this works is that
    First run : we add "aaaa" the pattern
    2nd run : we add "abab" in the pattern here and finally we get
    what we want

             */
            for (j in 0 until n / i) {
                pattern.append(s.substring(0, i))
            }
            if (s == pattern.toString()) {
                return true
            }
        }
    }
    return false
}