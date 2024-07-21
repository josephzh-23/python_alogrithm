'''
We use as said
Val1 and val2 represent the nodes of tree1 and tree2 respectively.


At each step we remove one pair from the stack and update tree1 in keeping with values within the pair.

2. If the left and right pointer of tree1 isn’t NULL we push them into the stack.

3. If the left child of tree1 is NULL, we update it with the left pointer of tree2.
The same goes for the right pointer.
'''
import site
from typing import Optional

from Binary_Search_Tree.BSTNode import TreeNode


# the 2 roots here
def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if root1 is None:
        return root2

    queue = [(root1, root2)]

    while len(queue):
        node1, node2 = queue.pop()
        if node1 is None or node2 is None:
            continue

        node1.val += node2.val

        if node1.left is None:
            node1.left = node2.left
            node2.left = None

        if node1.right is None:
            node1.right = node2.right
            node2.right = None

        queue.append((node1.left, node2.left))
        queue.append((node1.right, node2.right))

    return root1








