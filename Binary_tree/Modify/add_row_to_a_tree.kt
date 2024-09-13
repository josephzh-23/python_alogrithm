import Tree.Basic.TreeNode
import java.util.*
// Print this out to get an idea
fun main() {
    val r = TreeNode(4)
    r.left = TreeNode(2)
    r.left!!.left = TreeNode(3)
    r.left!!.right = TreeNode(1)
    // The tree node here is node.value
    r.right= TreeNode(6)
    addOneRow(r, 1, 5)
}

fun addOneRow(t: TreeNode, v: Int, d: Int): TreeNode {
    // Using this now a row has been added here
    // This is the root node here we make n the root
    if (d == 1) {
        val n = TreeNode(v)
        n.left = t
        return n
    }
    var queue: Queue<TreeNode> = LinkedList()
    queue.add(t)
    var depth = 1

    // This allows you to traverse up to that level here as said
    while (depth < d - 1) {

        val temp: Queue<TreeNode> = LinkedList()
        while (!queue.isEmpty()) {
            val node: TreeNode = queue.remove()
            //
            println("the node here is ${node.value}")
            if (node.left != null) temp.add(node.left)
            if (node.right != null) temp.add(node.right)
        }
        queue = temp
        println("queue here is ${queue.size}")
        depth++
    }
    while (!queue.isEmpty()) {
        val node: TreeNode = queue.remove()
        println("the head node is ${node.value}")
        var temp: TreeNode = node.left!!
        node.left = TreeNode(v)
        node.left!!.left = temp
        temp = node.right!!
        node.right = TreeNode(v)
        node.right!!.right = temp
    }
    return t
}