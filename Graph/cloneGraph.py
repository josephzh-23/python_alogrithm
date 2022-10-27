
class Node:
    def __init(s, val = 0, neighbors = None):
        s.val = val
        s.neighbors = neighbors #if neighbor is not None else []

# use a BFS for this
class Solution:
    def cloneGraph(s, node):

        if not node:
            return node
        firstVal = node.val

        # dictionary
        '''
          1: {1, [2, 4] }
        2: {2, []}
        '''
        oldNew = {
            firstVal: Node(firstVal, [])
        }
        q = []
        q.append(node)

        while q:
            cur = q.pop(0)
            curClone = oldNew[cur.val]

            for neighbor in cur.neighbors:  # 2:

                '''
                    if it doesn't exist already, we will make it 
                '''
                if neighbor.val not in oldNew:
                    oldNew[neighbor.val] = Node(neighbor.val, [])
                    q.append(neighbor)

                # add the neighbor to it
                curClone.neighbors.append(oldNew[neighbor.val])
        # return the first value
        return firstVal









