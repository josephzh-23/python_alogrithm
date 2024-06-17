'''

We will code the solutino first and then think about what it means here

- Using 2 queues here basically and then going here
-
'''
from collections import Counter, deque

from Heap import MinHeap
'''
Remember this is a hard problem ehre 
'''

# rearrange string here leetcode
def rearrangeStringKDistanceApart(s, k):
    freq = Counter(s)
    '''

    this queue will have all the characters that can be placed next,
     with the character having the highest frequency at the top.

     Will have <int, chara>
    '''
    free = MinHeap()
    for num, char in freq.items():
        free.push([char, num])
    ans = ""

    # this q stores the chars that can not be used now
    busy = deque()

    while len(ans) != len(s):
        index = len(ans)
        # // Insert the character that could be used now into the free heap.
        if busy and index - busy.__getitem__(0)[0] >= k:
            q= busy.pop()
            # we want the counter of that character that just popped
            free.push([freq.get(q[1]),q[1]] )

        if not free:
            return ""
        curchar = free.peek()[1]
        print('current char is ', curchar)

        free.pop()
        ans += curchar


        # insert the used char into the busy q with the cur index
        freq[curchar] = freq[curchar] -1
        if freq[curchar] > 0:
            busy.append([index, curchar])
    print('answer is', ans)
    return ans

rearrangeStringKDistanceApart("aabbcc", 3)






