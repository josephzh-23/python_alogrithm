'''

Using this problem here you have
'''
from collections import defaultdict, deque
from typing import List

from Binary_tree.BSTNode import TreeNode

def verticalOrder( root: TreeNode) -> List[List[int]]:
    if root is None:
        return []

    columnTable = defaultdict(list)
    min_column = max_column = 0
    queue = deque([(root, 0)])

    while queue:
        node, column = queue.popleft()

        if node is not None:
            columnTable[column].append(node.val)
            min_column = min(min_column, column)
            max_column = max(max_column, column)

            queue.append((node.l, column - 1))
            queue.append((node.r, column + 1))

    return [columnTable[x] for x in range(min_column, max_column + 1)]

# for each column index then add sth here as said already this is very important as said
# for x in sorted(columnTable.keys()):
#     res.append([columnTable[x]])

root = TreeNode(3)
root.l = TreeNode(9)
root.r = TreeNode(20)
root.r.l = TreeNode(15)
root.l.r = TreeNode(7)
print(verticalOrder(root))
