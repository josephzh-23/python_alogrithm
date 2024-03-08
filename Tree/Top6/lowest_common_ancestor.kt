package Tree.Top6

import Tree.Basic.TreeNode

// Find lowest common ancestor

/*
Time Complexity : O(N), where N is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.

Space Complexity : O(1)O(1).

What are the cases here?

Start traversing the tree from the root node.

Case 1
If both the nodes p and q are in the right subtree,
then continue the search with right subtree starting step 1.
C2:
If both the nodes p and q are in the left subtree, then continue the search with left subtree starting step 1.
C3:
If both step 2 and step 3 are not true, this means we have found the node which is common to node p's and q's subtrees. and hence we return this common node as the LCA.
 */
fun lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode): TreeNode? {
    val parentVal = root.value
    val pValue = p.value
    val qVal = q.value
    // Update the root
   // Check if in right tree
    if(p.value > root.value && q.value > root.value){

       return lowestCommonAncestor(root.right!!,p, q )

        // In the left case
    }else if(p.value < root.value && q.value < root.value){
        return lowestCommonAncestor(root.left!!,p, q )
    }else{
        return root
    }
}