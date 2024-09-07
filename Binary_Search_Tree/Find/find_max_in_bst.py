# Function to find the node with maximum value
# i.e. rightmost leaf node
def maxValue(root):
    current = root

    # loop down to find the rightmost leaf
    while (current.r):
        current = current.r
    return current.data


# fxn to find the max over here then lol