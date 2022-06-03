
'''
Using a fast and a slow pointer, they will eventually collide if there
is a loop, otherwise they won't collide
'''

def hasCycle(root):

    if not root:
        return False

    fast = root.next
    slow = root

    while fast and fast.next and slow:
        if fast == slow:
            return True

        # fast will move by 2 jumps 
        fast = fast.next.next
        slow = slow.next








