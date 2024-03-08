 package Tree

import Tree.Basic.TreeNode

// The TC will then be Time: O(n) and O(h)
fun mergeTrees(t1: TreeNode?, t2: TreeNode?): TreeNode?{
    if(t1 == null) return t1
    if(t2 == null) return t2

    // At this point both exist
    t1.value +=t2.value
    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t2.right, t2.right)
    return t1
}