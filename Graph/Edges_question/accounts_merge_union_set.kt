import Util.printList
import java.util.*


/*

ACcounts merge a problem better explanation here
dfs ->

SO the above solutino would give you
 */

class Solution23 {
     class UnionFind(num: Int) {
        var parent: IntArray
        var weight: IntArray

        init {
            parent = IntArray(num)
            weight = IntArray(num)
            for (i in 0 until num) {
                parent[i] = i
                weight[i] = 1
            }
        }

        fun union(a: Int, b: Int) {
            val rootA = findRoot(a)
            val rootB = findRoot(b)
            if (rootA == rootB) {
                return
            }
            if (weight[rootA] > weight[rootB]) {
                parent[rootB] = rootA
                weight[rootA] += weight[rootB]
            } else {
                parent[rootA] = rootB
                weight[rootB] += weight[rootA]
            }
        }
        // A new function here to find the root of the element
        fun findRoot(a: Int): Int {
            if (parent[a] == a) {
                return a
            }
            parent[a] = findRoot(parent[a])
            return parent[a]
        }
    }

}


fun main() {
    // So 1 element will act as an email here and then here
    // then
    var accounts = listOf(
        listOf("John","johnsmith@mail.com","john_newyork@mail.com"),
        listOf("John","johnsmith@mail.com","john00@mail.com"),
        listOf("Mary","mary@mail.com"),
        listOf("John","johnnybravo@mail.com")
    )

    printList(accountsMerge(accounts))

}


fun accountsMerge(accounts: List<List<String>>): List<List<String>?> {
    val size = accounts.size
    val uf = Solution23.UnionFind(size)
    // the following would be sth like this
    //

    /*

   email2AccountId = {
   joe@gmail.com: 0
   johna@gmail.com: 0
   a_joe@mail.com : 1           will be the above here
   joe_b@mail.com: 2
   joe_b@mail2.com: 2
     */
    // prepare a hash with unique email address as key and
    // index/position in accouts list as value
    val emailToId = HashMap<String, Int?>()
    for (i in 0 until size) {
        val details = accounts[i]
        for (j in 1 until details.size) {
            val email = details[j]

            // if we have already seen this email before, merge the account  "i" with previous account
            // else add it to hash
            if (emailToId.containsKey(email)) {
                emailToId[email]?.let { uf.union(i, it) }

                // So would be -> "john@gmail.com" -> 1
            } else {
                emailToId[email] = i
            }
        }
    }

    //This is the returning results
    val idToEmails = HashMap<Int, MutableList<String>?>()


    // For each email, get the id add the root
    // 0: "john@gmail.com"
    for (key in emailToId.keys) {

        // Check the root of each account index, and add the email it
        val root: Int = emailToId[key]?.let { uf.findRoot(it) }!!
        if (!idToEmails.containsKey(root)) {
            idToEmails[root] = ArrayList()
        }
        idToEmails[root]!!.add(key)
    }


    // merged accounts will be
    // mergedAccounts = [
    // [joe-a@gmail.com, john@gmail.com],
    // [mary@gmail.com, mary1@gmail.com]
    // collect the emails from idToEmails, sort it and add account name at index 0 to get the final list to add to final return List
    val mergedDetails: MutableList<List<String>?> = ArrayList()


    for (id in idToEmails.keys) {
        val emails: MutableList<String>? = idToEmails[id]
        Collections.sort(emails)
        emails?.add(0, accounts[id][0])
        mergedDetails.add(emails)
    }
    return mergedDetails
}