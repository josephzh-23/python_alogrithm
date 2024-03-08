import Util.printList
import java.util.*

fun main() {
    var accounts = listOf(
        listOf("John", "johnsmith@mail.com", "john_newyork@mail.com"),
        listOf("John", "johnsmith@mail.com", "john00@mail.com"),
        listOf("Mary", "mary@mail.com"),
        listOf("John", "johnnybravo@mail.com")
    )
    printList(accountsMergeDfs(accounts))
}


fun accountsMergeDfs(accounts: List<List<String>>): List<List<String?>> {
    val res: MutableList<List<String?>> = ArrayList()
    if (accounts.isEmpty()) return res
    val g: MutableMap<String, MutableSet<String>> = HashMap()
    val mailToName: MutableMap<String, String> = HashMap()


    buildGraph(g, accounts, mailToName)
    val visited: MutableSet<String> = HashSet()
    for (mail in mailToName.keys) {
        val name = mailToName[mail]


        val mails: MutableList<String> = ArrayList()
        if (!visited.contains(mail)) {

            dfsString(mails, mail, g, visited)
            mails.sort()
            name?.let {
                mails.add(0, it)
            }
            res.add(mails)
        }
    }
    return res
}

private fun dfsString(
    mails: MutableList<String>,
    mail: String,
    g: Map<String, MutableSet<String>>,
    visited: MutableSet<String>
) {
    mails.add(mail)
    if (g[mail]!!.size == 0) return
    for (neigh in g[mail]!!) {
        if (!visited.contains(neigh)) {
            dfsString(mails, neigh, g, visited)
        }
    }
}

private fun buildGraph(
    g: MutableMap<String, MutableSet<String>>,
    accounts: List<List<String>>,
    mailToName: MutableMap<String, String>
) {
    for (account in accounts) {
        val name = account[0]
        for (i in 1 until account.size) {
            val mail = account[i]
            mailToName[mail] = name
            g.putIfAbsent(mail, HashSet())
            if (i == 1) continue
            val prev = account[i - 1]
            g[prev]!!.add(mail)
            g[mail]!!.add(prev)
        }
    }
}