# Function to find the node with maximum value
# i.e. rightmost leaf node
def maxValue(root):
    current = root

    # loop down to find the rightmost leaf
    while (current.right):
        current = current.right
    return current.data


# fxn to find the max over here then lol