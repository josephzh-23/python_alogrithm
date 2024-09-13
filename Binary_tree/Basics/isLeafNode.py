# a function to check if is leaf node

def isLeafNode(node):
    if not node.l and not node.r:
        return True
    else:
        return False