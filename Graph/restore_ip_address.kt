package Graph

import java.util.*

class restore_ip_addresses {
    var res: MutableList<String> = LinkedList()
    fun restoreIpAddresses(s: String): List<String> {
        val n = s.length
        if (n == 0) {
            return res
        }
        dfs(StringBuilder(), s, 4)
//        print(res)
        return res
    }

    // As there would 4 sections here since we have 4 sections in the ip
    // addresses
    // str: the string builder each time
    /*
    s: string here  would gradually get smaller
     */
    private fun dfs(str: StringBuilder, s: String, sections: Int) {
        var str = str
        val n = s.length

        // We have reached the end and we have found 1 combination here

        if (n == 0 && sections == 0) {
            res.add(str.substring(0, str.length - 1).toString())
            return
        }
        val sb = StringBuilder()
        val min = Math.min(s.length, 3)
        if (n > 0 && sections == 0) return
        if (n == 0 && sections > 0) return

        // Up to the length 3
        for (i in 0 until min) {
//            println(s[i])
            sb.append(s[i])

            // Convert it to number here
            val value = sb.toString().toInt()
//            println(sb)

            // Basically take care of invalid cases here
            //take care of invalid cases of leading 0s and all that
            if (sb.length == 2 && value < 10) continue
            if (sb.length == 3 && value < 100) continue

            // An invalid value down here
            if (sb.length == 2 && value > 255) continue

            // If valid then try adding the . at the end
            // Ex: 1 -> 1.
            val temp = StringBuilder(str)
            str.append(sb)
            str.append('.')


            //
            dfs(str, s.substring(i + 1, s.length), sections - 1)

            // Each time it comes here either 1 combination has bee found or
            // no compbination has been found
            // reset our current string for the next backtracking here
            println(temp)
            str = temp
        }
    }
}

fun main() {
    var s = restore_ip_addresses()
    s.restoreIpAddresses("101023")
}