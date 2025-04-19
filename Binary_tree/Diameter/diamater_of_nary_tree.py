'''

Nary tree has any number of children here
- Between any 2 nodes in a tree,

- Doesn't include the root node itself here
-

The key steps here are :

1. Traverse each node with DFS, starting from the root.
2. For each node visited, calculate the
- m1 : lengths of the longest (max) and
 - m2: 2nd longest (smax) paths among its child nodes.

3.
We loop through each child of the current node and recursively call dfs(child).
 The returned value

 t :  the height of the subtree rooted at child. We use this value to potentially update m1 and m2.

If t is greater than m1,
 we set m2 to m1 and then m1 to t,
thus keeping m1 as the max height and m2 as the second max height among the children.

If t < m1 but is >  than m2, we update m2 with t.

After considering all children,
 we update the ans variable (which is kept in the outer scope of dfs and declared as nonlocal) with the maximum of its current value and the sum of m1 + m2, representing the potential diameter at this node (the longest path through the node)


The dfs function concludes by returning 1 + m1,

which represents the height of the subtree rooted at the current node
(1 for the edge connecting to its parent and m1 as the height of its longest subtree).


'''


def diameter(self, root: 'Node') -> int:
    # Helper function to perform depth-first search
    def dfs(node: 'Node') -> int:
        # base case: if the current node is None, return 0
        if node is None:
            return 0
        # accessing the non-local variable 'max_diameter' to update its value within this helper function
        nonlocal max_diameter

        # initialize the two longest paths from the current node to 0
        longest_path = second_longest_path = 0
        # iterate over all the children of the current node
        for child in node.children:
            # recursively find the longest path for each child
            path_length = dfs(child)


            # check if the current path is longer than the longest recorded path
            if path_length > longest_path:
                # update the second longest and longest paths accordingly
                second_longest_path, longest_path = longest_path, path_length


            # else if it's only longer than the second longest, update the second longest
            elif path_length > second_longest_path:
                second_longest_path = path_length


        # update the maximum diameter encountered so far based on the two longest paths from this node
        max_diameter = max(max_diameter, longest_path + second_longest_path)
        # return the longer path increased by 1 for the edge between this node and its parent
        return 1 + longest_path

    # Initialize max_diameter to 0 before starting DFS
    max_diameter = 0
    # Call the dfs function starting from the root node
    dfs(root)
    # Once DFS is complete, return the max_diameter found
    return max_diameter