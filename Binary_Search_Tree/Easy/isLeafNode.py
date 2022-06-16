# a function to check if is leaf node

def isLeafNode(node):
    if not node.left and not node.right:
        return True
    else:
        return False