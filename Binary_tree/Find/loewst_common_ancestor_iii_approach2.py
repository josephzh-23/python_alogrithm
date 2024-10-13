'''
Using approahc 2  O(1)

very simliar to problem 160 as said


Basically 2 pointers if one a runs out fist it will then switch to pb basically here
'''

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a, b = p, q
        while a != b:
            a = a.parent if a.parent else q
            b = b.parent if b.parent else p
        return a