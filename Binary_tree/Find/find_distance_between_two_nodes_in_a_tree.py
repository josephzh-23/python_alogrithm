'''


Find distance between two nodes of a Binary Tree
the # of nodes to be traversed between 2 trees when no parent pointer is given

        1
      /  \
     2    3
    /\   / \
   4  5  6  7
         \
          8

  Can be done using LCA here

  We first find the LCA of two nodes.
   Then we find the distance from LCA to two nodes.

   This solutino has a O(n) run time here

'''


class Node:
    # Constructor to create new node
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# step 2
# from the ancestor node to the data
def find_distance_from_ancestor_node(root: Node, data: int) -> int:
    # case when we reach a beyond leaf node
    # or when tree is empty
    if root is None:
        return -1

    # Node is found then return 0
    if root.data == data:
        return 0

    left = find_distance_from_ancestor_node(root.left, data)
    right = find_distance_from_ancestor_node(root.right, data)
    distance = max(left, right)
    return distance + 1 if distance >= 0 else -1




# step 1 here
# function to find distance between two
# nodes in a binary tree

def find_distance_between_two_nodes(root: Node, n1: int, n2: int):
    lca = find_least_common_ancestor(root, n1, n2)

    return find_distance_from_ancestor_node(lca, n1) + find_distance_from_ancestor_node(lca, n2) if lca else -1




# step 3
def find_least_common_ancestor(root: Node, n1: int, n2: int) -> Node:
    # Base case
    if root is None:
        return root

    # If either n1 or n2 matches with root's
    # key, report the presence by returning root
    if root.data == n1 or root.data == n2:
        return root

    # Look for keys in left and right subtrees
    left = find_least_common_ancestor(root.left, n1, n2)
    right = find_least_common_ancestor(root.right, n1, n2)

    if left and right:
        return root

    # Otherwise check if left subtree or
    # right subtree is Least Common Ancestor
    if left:
        return left
    else:
        return right

# function to find distance of any node
# from root


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

print("Dist(4,5) = ", find_distance_between_two_nodes(root, 4, 5))
print("Dist(4,6) = ", find_distance_between_two_nodes(root, 4, 6))
print("Dist(3,4) = ", find_distance_between_two_nodes(root, 3, 4))
print("Dist(2,4) = ", find_distance_between_two_nodes(root, 2, 4))
print("Dist(8,5) = ", find_distance_between_two_nodes(root, 8, 5))

#