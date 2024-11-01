'''
Let's focus on this one here

Return the vertical order traversal of its nodes


Create a dict

1. Create a dictonary with the column index, val: [value of all nodes] that share the same index
2. Each item in list contains value of a node ordered by row indices

1. If do bfs from root, root be at col 0, keep in root the ndoe and the column here
2. [ Store the value in column index here, root val should be at index 0 here

3. Node on left: col- 1
    Node on right

4.
'''
from collections import defaultdict, deque
from typing import List

from Binary_tree.BSTNode import TreeNode


# shoudl be from left tor ight here

# and here comes the data here that's number 1
def verticalOrder(self, root: TreeNode) -> List[List[int]]:
    columnTable = defaultdict(list)
    queue = deque([(root, 0)])

    while queue:
        node, column = queue.popleft()

        if node is not None:
            columnTable[column].append(node.val)

            queue.append((node.l ,column - 1))
            queue.append((node.r, column + 1))


    for x in range(min)