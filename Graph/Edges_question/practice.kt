//package Graph.Union_set
//
//
//fun main() {
//
//    var accounts = listOf(
//        listOf("John","johnsmith@mail.com","john_newyork@mail.com"),
//        listOf("John","johnsmith@mail.com","john00@mail.com"),
//        listOf("Mary","mary@mail.com"),
//        listOf("John","johnnybravo@mail.com")
//    )
//
//    // Once you have all these accounts here
//    var union = Solution23.UnionFind(4)
//    for(account in accounts){
//
//        if(account.size >= 2){
//            union.union(account[1], account[2])
//        }
//    }
//}
