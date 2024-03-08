package String_manipulation

import January_3rd.print
import java.lang.Integer.min

/*

This is the question from eric programming pramp video
If given 2 words, then find the min # of characters you need to delete
to make them the same
"heat" and "hit" are then 3 delete 'e', 'a', and 'i'

 */
// TC: O(len(str1) * len(str2))

fun main() {
    var a = Sol()
    a.minDeletionDistance("heat", "hit").print()
}
class Sol() {
    lateinit var arr1: CharArray
    lateinit var arr2: CharArray
    fun minDeletionDistance(str1: String, str2: String):Int {
        arr1 = str1.toCharArray()
        arr2 = str2.toCharArray()
        return dfs(0, arr1.size, 0, arr2.size)
    }
    var minDeletion = 0
    private fun dfs(start1: Int, end1: Int, start2: Int, end2: Int) :Int{
        if(start1 == end1 && start2 == end2) return 0
        if(start1 == end1) return end2 - start2
        // This covers the case where str1 = "12" str2 = ""
        if(start2== end2) return end1 - start1

        if(arr1[start1] == arr2[start2]){
            return dfs(start1 +1, end1, start2 + 1, end2 )
        }else{
            val path1 = dfs(start1 + 1, end1, start2, end2)
            val path2 = dfs(start1 , end1, start2 + 1, end2)
            minDeletion = min(path1, path2)
            return minDeletion
        }
    }
}