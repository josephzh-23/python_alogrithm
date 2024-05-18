package Tree.Subtree

import Tree.Basic.TreeNode

// Function to find
// largest subtree sum.

var res = 0
fun findLargestSubtreeSum(root: TreeNode?): Int {
    // If tree does not exist,
    // then answer is 0.
    if (root == null) return 0

    // Variable to store
    // maximum subtree sum.
    var ans = Int.MIN_VALUE

    // Call to recursive function
    // to find maximum subtree sum.
    ans = findLargestSubtreeSumUtil(root, ans)
    return ans
}

fun findLargestSubtreeSumUtil(root: TreeNode?,
                              ans: Int): Int {
    var ans = ans
    // If current node is null then
    // return 0 to parent node.
    if (root == null) return 0

    // Subtree sum rooted
    // at current node.
    val currSum: Int = root.value + findLargestSubtreeSumUtil(root.left, ans) + findLargestSubtreeSumUtil(root.right, ans)

    // Update answer if current subtree
    // sum is greater than answer so far.
    ans = Math.max(ans, currSum)

    // Return current subtree
    // sum to its parent node.
    return currSum
}
// Driver Code
fun main(args: Array<String>) {
    /*
            1
            / \
            /     \
        -2     3
        / \     / \
        / \ / \
        4     5 -6     2
    */
    val root = TreeNode(1)
    root.left = TreeNode(-2)
    root.right = TreeNode(3)
    root!!.left!!.left = TreeNode(4)
    root.left!!.right = TreeNode(5)
    root.right!!.left = TreeNode(-6)
    root.right!!.right = TreeNode(2)
    println(findLargestSubtreeSum(root))
}