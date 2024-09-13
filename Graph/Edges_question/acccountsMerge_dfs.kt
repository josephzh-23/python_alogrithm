package Graph.Union_set

import java.util.*


fun main() {

}
fun acccountsMerge(
    accounts: List<List<String>>
) {

    var mailToName = mutableMapOf<String, String>()

    // Basically an email will then have a string
    // and a list of neighbors here

    var g = mutableMapOf<String, MutableSet<String>>()
    //
    for (account in accounts) {
        val name = account[0]
        // Will get you a
        for (i in accounts.indices) {
            val mail = account[i]
            mailToName[mail] = name
            if (i == 1) continue

            // Will then skip the loop here
            var prev = account[i - 1]
            g.computeIfAbsent(prev) { HashSet() }.add(mail)
            g.computeIfAbsent(mail) { HashSet() }.add(prev)
        }
    }


    var res = ArrayList<MutableList<String>>()
    var visited = mutableSetOf<String>()
    for (mail in mailToName.keys) {

        val name = mailToName[mail]
        // So for each mail you would have a list of mails
        //
        var mails = mutableListOf<String>()
        if (!visited.contains(mail)) {
            dfsString(mails, mail, g, visited)
            if (name != null) {

                // This makes sure to insert the name at the 0th index
                // and then push everything back

                /*
                This will add sth liek the one below:
                "johnsmith@mail.com","john_newyork@mail.com", "john00@mail.com"
                 */
                mails.sort()
                mails.add(0, name)
                res.add(mails);
            }
        }
    }
}


// Traverse through all the neighbors of an email say
// Say "john@gmail.com" and all its neighbors here
fun dfsString(
    mails: MutableList<String>,
    mail: String,
    g: MutableMap<String, MutableSet<String>>,
    visited: MutableSet<String>
) {

    mails.add(mail)
    if (g[mail] == null || g[mail]!!.size == 0) return
    g[mail]?.let {
        for (neighbor in it) {
            if (!visited.contains(neighbor)) {
                dfsString(mails, neighbor, g, visited)
            }
        }
    }
}


