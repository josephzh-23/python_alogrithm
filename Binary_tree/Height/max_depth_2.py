from Binary_tree.BSTNode import TreeNode


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
def height(root):
    if root is None:
        return -1

    # compute the height of left and right subtrees
    lHeight = height(root.left)
    rHeight = height(root.right)
    print('the left and right heights are' ,lHeight, rHeight)
    return max(lHeight, rHeight) + 1


if __name__ == "__main__":
    # Representation of the input tree:
    #     12
    #    /  \
    #   8   18
    #  / \
    # 5   11
    root = Node(12)
    root.left = Node(8)
    root.right = Node(18)
    root.left.left = Node(5)
    root.left.right = Node(11)

    print(height(root))


