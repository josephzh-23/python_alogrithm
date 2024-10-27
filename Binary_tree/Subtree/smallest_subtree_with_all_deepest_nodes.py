'''

This is 865 problem here

Depth of each node : shortest distance to the root of the tree

A node is called the deepest if it has the largest depth possible
 among any node in the entire tree.
'''


def subtreeWithAllDeepest(self, root):
    # Tag each node with it's depth.
    depth = {None: -1}

    def dfs(node, parent=None):
        if node:
            depth[node] = depth[parent] + 1
            dfs(node.left, node)
            dfs(node.right, node)

    dfs(root)
    max_depth = max(depth.itervalues())

    # this will recursively call the lowest element in the list so be careful here 
    def answer(node):
        # if depth of the answer is
        if not node or depth.get(node, None) == max_depth:
            return node
        L, R = answer(node.left), answer(node.right)
        return node if L and R else L or R

    return answer(root)