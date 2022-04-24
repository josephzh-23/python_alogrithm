
"""
Heap with N elements has height = Log2N
    N = 6       height = 2

i: the index of child node

    Parent position = i/2
    Left child position = 2i
    Right child position = 2i + 1
"""


# i: the index of the node in interest


def heapify(arr, n, i):
    parent = int(((i - 1) / 2))

    # For Max-Heap
    # If current node is greater than its parent
    # Swap both of them and call heapify again
    # for the parent

    if arr[parent] > 0:

        # If the child node > parent, then swap
        if arr[i] > arr[parent]:

            arr[i], arr[parent] = arr[parent], arr[i]
            # Recursively heapify the parent node
            heapify(arr, n, parent)


# Function to insert a new node to the Heap


def insertNode(arr, key):
    global n
    # Increase the size of Heap by 1
    n += 1

    # Insert the element at end of Heap
    arr.append(key)
    # Heapify the new node following a
    # Bottom-up approach
    heapify(arr, n, n - 1)


# A utility function to print array of size n


def printArr(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


# Driver Code
# Array representation of Max-Heap
'''
        10
       /  \
      5    3
     / \
    2   4
'''
arr = [10, 5, 3, 2, 4, 1, 7]
n = 7
key = 15
insertNode(arr, key)
printArr(arr, n)
# Final Heap will be:
'''
      15
    /   \
   5     10
 /  \    /
2    4   3

Code is written by Rajat Kumar....

'''