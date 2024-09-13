package Tree.Hard

import Tree.Basic.TreeNode



/*

You are given the root of a binary tree and an integer distance.
 A pair of two different leaf nodes of a binary tree is said to be good if the
 length of the shortest path between them is less than or equal to distance.
 */
/*
Please see notes, need to use a post order approach here
 */
internal class Solution133 {

    // Count the number of pairs here in the graph as said
    var pairs = 0
    fun countPairs(root: TreeNode?, distance: Int): Int {
        var list = helper(root, distance)
        list.forEach {
            println(it)
        }
        return pairs
    }

    fun helper(root: TreeNode?, distance: Int): List<Int> {
        val l: MutableList<Int> = ArrayList()
        if (root == null) return l

        // Add 1 to the start for each leaf node
        if (root.left == null && root.right == null) {
            l.add(1)
            return l
        }

        // For each level this will be [1, 1]
        val leftDepth = helper(root.left, distance)
        val rightDepth = helper(root.right, distance)
        val newList: MutableList<Int> = ArrayList()

        // Once left and right is done
        for (i in leftDepth.indices) {
            for (j in rightDepth.indices) {
//                println("${leftDepth[i]} + ${rightDepth[j]}")
                if (leftDepth[i] + rightDepth[j] <= distance) pairs++
            }
        }

        // Here we have finished traversing 1 level basically

        // Here we are adding 1 to each left and right depth
        // basically we are going back up 1 level

        // [1, 1] -> [2, 2]     since we are going higher 1 branch
        println("here")

        for (num in leftDepth) if (num + 1 <= distance) newList.add(num + 1)
        for (num in rightDepth) if (num + 1 <= distance) newList.add(num + 1)

        return newList
    }
}

fun main() {
    var s = Solution133()
    val r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    r.left!!.left = TreeNode(4)
    r.left!!.right = TreeNode(5)
    r.right!!.left = TreeNode(6)
    r.right!!.right = TreeNode(7)
    s.countPairs(r, 3)

//    val r = Tree.Basic.TreeNode(1)
//    r.left = Tree.Basic.TreeNode(2)
//    r.right = Tree.Basic.TreeNode(3)
//    r.left!!.right = Tree.Basic.TreeNode(4)
//    s.countPairs(r, 3).print()
}