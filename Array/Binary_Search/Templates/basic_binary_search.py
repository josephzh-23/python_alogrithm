'''

Basic binary search here and will then have the data that we need to take care of here

bisect.bisect_left([1,2,3], 2)
1
bisect.bisect_right([1,2,3], 2)
2
'''
import bisect
from typing import List

'''
bisect rigth is the same as bisect : basically using bisect lets you know where to insert
that particular element in this array here 

bisect_left makes sure it's just 1 index to the left here 

'''
original = bisect.bisect([1, 2, 3], 5)
a = bisect.bisect_right([1, 2, 3], 2)
b = bisect.bisect_left([1, 2, 3], 2)

'''

'''
print('c is', original , 'a is ', a, 'b is', b)


