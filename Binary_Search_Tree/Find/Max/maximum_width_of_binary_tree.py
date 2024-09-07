'''

Appraoch #1:
The node then becomes
          A
       /   \
      B     C
     / \   / \
    D   E F   G

Need to serialize the tree first here, mark A as 0

Now we can mark nodes D, E, F, G with 3, 4, 5, and 6

1.  So mark the tree in the following way:
left child = 2*(marked value of parent node)+ 1 and right child = 2*(marked value of parent node) + 2
but if the tree kept on growing it’ll lead to huge numbers, this is not good here


Approach #2:
So better approach:

Level 1: We’re marking the root node with 0
Level 2: Node 2 and 3 will be marked 1 and 2 respectively.

Level 3: We’ll subtract 1 from the marked serials of both node 2 and 3, and then will mark their children accordingly.

node 4: 2*(marked value of node 2 — 1) + 1 = 1
node 5: 2*(marked value of node 2 — 1) + 2 = 2

node 6: 2*(marked value of node 3 — 1) + 1 = 3
node 7: 2*(marked value of node 3 — 1) + 2 = 4

And once the above is done
'''


def widthOfBinaryTree(r):
    res = []

    # we want to push into this the node and the index of the node right there
    q = []

    maxwidth = 0 # at the front here

    if not r: return 0

    q.append([r, 0])

    while q:
        nodesPerLevel = []

        # the one at the top here
        first, last = q[-1]

        maxwidth = max(maxwidth, last - first + 1)
        for i in range(len(q)):

            node = q[-1][0]

            # the serial number here
            hackSerial = q[-1][1] - 1
            q.pop()
            nodesPerLevel.append(node.val)
            if node.left:
                q.append([node.l, 2 * hackSerial + 1])
            if node.right:
                q.append([node.r, 2 * hackSerial + 1])
        res.append(nodesPerLevel)

        #return the max width here as said
    return maxwidth
