package Tree

import Tree.Basic.TreeNode

//O (m) or O (n) where m and n are # of nodes of each tree
//# as explained already

fun isSameTree(p: TreeNode, q: TreeNode):Boolean{
    //If both trees are empty then return true
    if(p==null && q==null) {
        return true

    }
    // if both trees are non-empty and the value of their root node matches,
    // recur for their left and right subtree
    return (p != null && q!= null) && (p.value== q.value) &&
            isSameTree(p.left!!, q.left!!) &&
            isSameTree(p.right!!, q.right!!);
}