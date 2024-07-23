package Tree.Count

import Tree.Basic.TreeNode

internal class Solution33 {
    var count = 0
    var k = 0
    var h: HashMap<Int?, Int?> = HashMap()
    fun preorder(node: TreeNode?, currSum: Int) {
        var currSum = currSum
        if (node == null) return
        currSum += node.value
        if (currSum == k) count++

        /*

        take node
        10 -> 5 -> 3->
        k will always be 8, when we get to 10 + 5 + 3 = 18
        take 18- 8 = 10

        Since
        if 10 is in the map, then add 1 to this count, this means
        we have found 1 sum already
         */
        count += h.getOrDefault(currSum - k, 0)!!

       // h[10] = 1
        h[currSum] = h.getOrDefault(currSum, 0)!! + 1
        preorder(node.left, currSum)
        preorder(node.right, currSum)

        // remove the current sum from the hashmap
        // in order not to use it during
        // the parallel subtree processing
        h[currSum] = h[currSum]!! - 1
    }

    fun pathSum(root: TreeNode?, sum: Int): Int {
        k = sum
        preorder(root, 0)
        return count
    }
}