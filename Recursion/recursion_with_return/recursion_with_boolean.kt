package Recursion.recursion_with_return

import Tree.Basic.TreeNode

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