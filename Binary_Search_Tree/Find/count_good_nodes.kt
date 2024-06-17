import Tree.Basic.TreeNode

/*
Use the preorder approach, center -> left tree and right tree

A good node is the greatest value seen among a subtree
    1
 2      3       3 is a good node

1. Keep track of the greatest value seen so far
2. So if >= max, then good node
3. Else bad node
 */
internal class Sol {
    private var numGoodNodes = 0
    fun countGoodNodes(root: TreeNode): Int {
        dfs(root, Int.MIN_VALUE)
        return numGoodNodes
    }

    private fun dfs(node: TreeNode, maxSoFar: Int) {
        if (maxSoFar <= node.value) {
            numGoodNodes++
        }
        if (node.right != null) {
            dfs(node.right!!, Math.max(node.value, maxSoFar))
        }
        if (node.left != null) {
            dfs(node.left!!, Math.max(node.value, maxSoFar))
        }
    }
}

fun main (){
    var s = Sol()

    val root = TreeNode(3)
    root.left = TreeNode(1)
    root.left?.left = TreeNode(3)
    root.right = TreeNode(4)
    root.right?.left = TreeNode(1)
    root.right?.right = TreeNode(5)
    s.countGoodNodes(root)

}

