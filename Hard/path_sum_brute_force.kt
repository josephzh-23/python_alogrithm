package Hard

import Tree.Basic.TreeNode
//https://leetcode.com/problems/path-sum-iii/
//Will work on path 3 problem leetcode

internal class Solution {
    var result = 0
    fun pathSum(root: TreeNode?, sum: Int): Int {
        dfs(root, sum)
        return result
    }

    fun dfs(node: TreeNode?, sum: Int) {
        if (node == null) {
            return
        }
        sum(node, sum)
        dfs(node.left, sum)
        dfs(node.right, sum)
    }

    fun sum(n: TreeNode?, s: Int) {
        if (n == null) {
            return
        }
        val temp: Int = s - n.value
        if (temp == 0) {
            result++
        }
        sum(n.left, temp)
        sum(n.right, temp)
    }
}
