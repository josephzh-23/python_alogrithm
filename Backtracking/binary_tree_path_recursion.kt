
import Tree.Basic.TreeNode
import java.util.*

/*
The most intuitive way is to use a recursion here.

 One is going through the tree by considering at each step the node itself
  and its children.
   Situation 1:
   If node is not a leaf, one extends the current path by a node
   value and calls recursively the path construction for its children.

   Situation 2
   If node is a leaf, one closes the current path and adds it into the list of paths.
 */
// This is just preorder traversal
// path: a string var
// https://leetcode.com/problems/binary-tree-paths/
/*
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]      is the above situation here
 */
fun construct_paths(root: TreeNode?, path: String?, paths: LinkedList<String?>) {


    var path = path
    if (root != null) {

        // Grab the value from the string here and then add it in the above
        // path and then once added
        path += Integer.toString(root.value)
        if (root.left == null && root.right == null) // if reach a leaf
            paths.add(path) // update paths
        else {
            path += "->" // extend the current path
            construct_paths(root.left, path, paths)
//            println(path)
            construct_paths(root.right, path, paths)
//            println(path)
        }
    }
}

fun binaryTreePaths(root: TreeNode?): List<String?>? {
    val paths: LinkedList<String?> = LinkedList<String?>()
    construct_paths(root, "", paths)
    return paths
}
fun main() {
    val root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left!!.left = TreeNode(4)
    root.left!!.right = TreeNode(5)
//     [1->2->5, 1->3]      the supposed answer
//    binaryTreePaths(root)
    println(binaryTreePaths(root))
//    preorder(root)
}
