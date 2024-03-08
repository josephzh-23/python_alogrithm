package Tree

import Tree.Basic.TreeNode
import java.util.*


// Will traverse between the files here
//
// Use a boolean that gets turned false or true as you traverse
// thru each level

internal object TUF {
    fun zigzagLevelOrder(root: TreeNode?): ArrayList<ArrayList<Int>> {
        val q: Queue<TreeNode?> = LinkedList()
        val wrapList = ArrayList<ArrayList<Int>>()
        if (root == null) return wrapList
        q.offer(root)
        var leftToRight = true
        while (!q.isEmpty()) {
            val levelNum = q.size
            val subList = ArrayList<Int>(levelNum)
            for (i in 0 until levelNum) {

                // We actually can't call remove here it would throw an exception
//                val index = i
//                val cur = q.remove()
                if (q.peek()!!.left != null) q.offer(q.peek()!!.left)
                if (q.peek()!!.right != null) q.offer(q.peek()!!.right)
                if (leftToRight == true) subList.add(q.poll()!!.value) else subList.add(0, q.poll()!!.value)
            }
            leftToRight = !leftToRight
            wrapList.add(subList)
        }
        return wrapList
    }

    @JvmStatic
    fun main(args: Array<String>) {
        var i: Int
        var j: Int
        val root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right!!.left = TreeNode(15)
        root.right!!.right = TreeNode(7)
        val ans: ArrayList<ArrayList<Int>>
        ans = zigzagLevelOrder(root)
        println("Zig Zag Traversal of Binary Tree ")
        i = 0
        while (i < ans.size) {
            j = 0
            while (j < ans[i].size) {
                print(ans[i][j].toString() + " ")
                j++
            }
            println()
            i++
        }
    }
}