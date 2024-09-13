package Tree

import Tree.Basic.TreeNode
import java.util.*
import kotlin.collections.ArrayList

fun printBottomView(r: TreeNode) {

    var results = ArrayList<TreeNode>()
    if (r == null) {
        return
    }

    var q = LinkedList<TreeNode>()
    r?.let {
        q.add(it)
    }
    while (!q.isEmpty()) {
        for (i in 0 until q.size) {
            val cur = q.remove()
            cur.left?.let {
                q.add(it)
            }
            cur.right?.let {
                q.add(it)
            }
            if(cur.left==null && cur.right==null){

                results.add(cur)
            }
        }

    }
    results.forEach {
        println(it.value)
    }

}

fun main(){
    val root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left!!.left = TreeNode(4)
    root.right!!.left = TreeNode(5)
    root.right!!.right = TreeNode(6)
    root.right!!.left!!.left = TreeNode(7)
    root.right!!.left!!.right = TreeNode(8)
    printBottomView(root)
}