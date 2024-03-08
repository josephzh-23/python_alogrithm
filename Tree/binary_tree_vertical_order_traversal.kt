package Tree

import java.util.*
import kotlin.collections.ArrayList







// So when you have a list of here
private class TreeNode(var value: Int,var y: Int,
        var left: TreeNode?, var right: TreeNode?){


}


// The level order traversal here
private fun levelOrder(r: TreeNode?): List<List<Int>> {

    val columnTable = mutableMapOf<Int, ArrayList<Int>>()
    val q :Queue<Pair<TreeNode?, Int>> = LinkedList()

    var column =0

    // step 1, add to the q as in all else
    q.offer(Pair(r, column))
    var results = ArrayList<List<Int>>()


    if (r == null) {
        return results
    }

    while (!q.isEmpty()) {

        // We poll from this and we get

        val (root, column) = q.poll()

        if(root!=null){
            columnTable.putIfAbsent(column, ArrayList())
            columnTable[column]?.add(root.value)

            // The column before the one on the right
            // And then the next column the one on the right
            q.offer(Pair(root.left, column -1))
            q.offer(Pair(root.right, column +1))
        }

    }

    
    var sortedKey =ArrayList(columnTable.keys)
    sortedKey.sort()

    for(k in sortedKey){
        columnTable[k]?.let { results.add(it) }
    }
    return results
}


