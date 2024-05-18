//package Tree
//
///*
//
  /* Construct the following tree
              1
            /   \
          2       3
         /      /   \
       4      5      6
             / \
            7   8
preorder: 1 2 4 3 5 7 8 6       r, left, right
inorder   4 2 1 7 5 8 6 3       left, r, right
postOrder  4 2 7 8 5 6 3 1      root comes in last, left, right, root

In order:
Traverse the left subtree, i.e., call Inorder(left->subtree)
Visit the root.
Traverse the right subtree, i.e., call Inorder(right->subtree)
// */
// */
//
// */