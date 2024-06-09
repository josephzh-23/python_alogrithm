'''

Using queue here then we have the code
'''
from collections import deque

q = deque()
q.append([4, 3])
print(q.__getitem__(0)[0])
print(q)