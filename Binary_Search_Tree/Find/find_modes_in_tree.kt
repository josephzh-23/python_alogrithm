package Tree.Top6

import Tree.Basic.TreeNode

// this will get you the nodes with the highest frequency here
internal class Solution10 {
    var prev: Int? = null
    var count = 1
    var max = 0
    fun findMode(root: TreeNode?): IntArray {
        val modes =  mutableListOf<Int?>()
        traverse(root, modes)
        val result = IntArray(modes.size)
//        for (i in modes.indices) {
//            result[i] = modes[i]!!
//        }
        return result
    }

    fun traverse(node: TreeNode?, modes: MutableList<Int?>) {
        if (node == null) return
        traverse(node.left, modes)

        // This is when you are processing the root element
        if (prev != null) {
            if (prev == node.value) {
                count++
            } else {
                count = 1
            }
        }

        // Compare the count and the maximum here
        if (count > max) {
            max = count
            modes.clear()
            modes.add(node.value)
        } else if (count == max) {
            modes.add(node.value)
        }

        prev = node.value
        traverse(node.right, modes)
    }
}

fun main() {
    var s = Solution10()
    val root = TreeNode(1)
    root.left = TreeNode(8)
    root.left?.left = TreeNode(8)
    root.left?.left?.right = TreeNode(831)
    root.left?.left?.right?.left = TreeNode(5)
    root.left?.left?.right?.right = TreeNode(6)
    root.right = TreeNode(7)
    root.right?.right = TreeNode(8)
    root.right?.right?.left = TreeNode(9)
    root.right?.right?.left?.left = TreeNode(10)
    root.right?.right?.left?.right = TreeNode(11)
    s.findMode(root).forEach{
        println(it)
    }
}