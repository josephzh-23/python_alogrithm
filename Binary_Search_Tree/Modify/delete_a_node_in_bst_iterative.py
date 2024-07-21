




'''

The solution below handles the problem of deleting a node in an easy way. The main idea of the code is the following:

Search the BST looking for our target node for deletion. (And exit if it'not present). A while-loop is used for this process.

After finding our target node, we notice that all nodes in the left-branch (node.left) are lower than anything at the right-side (node.right). This property can be used to:

Place the right-side branch as the main sub-tree.
Insert the former left-branch (node.left) at the left-most available position in our new sub-tree (node.right).
Edge Cases for (2):


If either node.left or node.right is missing for our target node, we use the existing branch as the new sub-tree.
If both branches are missing (leaf target), we use replace our target node by a Null value.
Now, to complete the deletion process, we insert/register our new-subtree in the parent of our "target node" (taking its place). If the deleted node was the root itself, we return None.

I hope the explanation was helpful. Cheers,



'''
class Solution:
    def deleteNode(self, root, key):
        # Search for our target node "n"
        n,par = root, None # n is our target for deletion (after iterating), par is its parent node
        while n and n.val!=key: # Traverse... while n is valid, and it doesn't match the key
            par = n
            n   = n.left if key < n.val else n.right
        if not n:
            return root # Key not Found
        #
        # Deletion: 4 Main Cases
        if (not n.left) and (not n.right):
            # A) Leaf Detected. Delete 100%
            new = None
        elif not n.left:
            # B) Left Branch Empty. Keep Right Branch.
            new = n.right
        elif not n.right:
            # C) Right Branch Empty. Keep Left Branch.
            new = n.left
        else:
            # D) Both branches exist. Make Right Branch Official, and place n.left and its left-most side.
            new = n.right
            # Find left-most side of n.right
            n2 = new
            while n2.left:
                n2 = n2.left
            # Place n.left at the left of our "new" sub-tree
            n2.left = n.left
        #
        # Insertion: 3 Cases
        if not par:
            # A) root node was deleted, return "new" sub-tree
            return new
        if par.left == n:
            # B) Replace "par.left" with our "new" sub-tree.
            par.left = new
        else:
            # C) Replace "par.right" with our "new" sub-tree.
            par.right = new
        return root