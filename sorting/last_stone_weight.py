'''
Stones stone[i] = the weight of the stone
Choose 2 wegiths together and smash

[2, 7, 4, 1, 8, 1]

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At each turn choose the heavist stone here (heavist) that should tell you a lot here

Can also be done using counting sort here 
'''

from sorting.minheap_template import MaxHeap


def lastStoneWeight(arr):
    h = MaxHeap()

    for i in arr:
        h.push(i)

    # while heap contains more than 1 stone here:
    while len(h) > 1:
        # 2 heavist stone
        x, y = h.pop(), h.pop()
        z = 0
        if (x==y):
            z= 0
        elif(x!=y):
            x = 0
            y-=x

        # the remaning y here
        h.push(y)
    if len(h) == 0:
        return 0
    return h.peek()
lastStoneWeight([2, 7, 4, 1, 8, 1])












