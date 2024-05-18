package Tree.Top6

import Tree.Basic.TreeNode


/*

An article also for this problem

https://takeuforward.org/data-structure/boundary-traversal-of-a-binary-tree/

My plan might seem a little bit of an overkill for a problem
like this so let's see the actual solutino

So the bounded here

TC: O(h) + O(h)     for left and right boundary traversal
+ O(n) for adding leaves the simple part        O (n) would be

// And then this is the answer as expected.

1. Simpler approach check left keep going left if null
then go right
1. What you want is the left boundary, excluding leaf nodes
2. Then take the leaf nodes
3. Then take the right boudnary reverse direction from bottom up

Take root of tree and put there
1. Add all the left first
2. If no left -> add right once reach leaf node then exclude it

3. So need to do an in order traversal here, add the leaf nodes
4. For right boundary   [would be in reverse order ]
    - check for right and then add to stack and stop at the
    leaf nodes

5.
 */


fun isLeaf(root: TreeNode): Boolean {
    return root.left == null && root.right == null
}

// add everything except for the leaf here
fun addLeftBoundary(root: TreeNode, res: ArrayList<Int>) {
    var cur: TreeNode? = root.left
    while (cur != null) {
        if (isLeaf(cur) == false) res.add(cur.value)

        // Move to right if no left
        cur = if (cur.left != null) cur.left else cur.right
    }
}

fun addRightBoundary(root: TreeNode, res: ArrayList<Int>) {

    var cur: TreeNode? = root.right
    val tmp = ArrayList<Int>()
    while (cur != null) {
        if (isLeaf(cur) == false) tmp.add(cur.value)
        cur = if (cur.right != null) cur.right else cur.left
    }

    var i: Int
    // Right after this we will take the reverse of the right
    // and add to our list
    i = tmp.size - 1
    while (i >= 0) {
        res.add(tmp[i])
        --i
    }
}

fun addLeaves(root: TreeNode, res: ArrayList<Int>) {
    if (isLeaf(root)) {
        res.add(root.value)
        return
    }
    if (root.left != null) addLeaves(root.left!!, res)
    if (root.right != null) addLeaves(root.right!!, res)
}

fun printBoundary(node: TreeNode): ArrayList<Int> {
    val ans = ArrayList<Int>()
    if (isLeaf(node) == false) ans.add(node.value)
    addLeftBoundary(node, ans)

    // The only one that has the recursive attached pretty
    // awesome stuff
    addLeaves(node, ans)
    addRightBoundary(node, ans)
    return ans
}

fun main(args: Array<String>) {
    val root = TreeNode(1)
    root.left = TreeNode(2)
    root.left?.left = TreeNode(3)
    root.left?.left?.right = TreeNode(4)
    root.left?.left?.right?.left = TreeNode(5)
    root.left?.left?.right?.right = TreeNode(6)
    root.right = TreeNode(7)
    root.right?.right = TreeNode(8)
    root.right?.right?.left = TreeNode(9)
    root.right?.right?.left?.left = TreeNode(10)
    root.right?.right?.left?.right = TreeNode(11)
    val boundaryTraversal: ArrayList<Int>
    boundaryTraversal = printBoundary(root)
    println("The Boundary Traversal is : ")
    for (i in boundaryTraversal.indices) {
        print(boundaryTraversal[i].toString() + " ")
    }
}