
'''

THis is the brute force approach here

'''
from typing import List


def decrypt( code: List[int], k: int) -> List[int]:
    n = len(code)

    sums = [0] * n
    if k == 0:
        return sums

    if k > 0:

        '''
        At i = 0 
        s = 7 + 1 + 4 
        = 12
        '''
        s = sum(code[1: k + 1])
        '''
        This is the sliding window here 
        '''
        for i in range(n):
            sums[i] = s
            '''
            if i = 0 
            To prepare for the next s:
            minus the code[i + 1] 
            (i + 1) % 4 = 1
            
            (i + 1 + k) % 4 = (1 + 3) %4 = 0
            
            s = s - code[1] + code[0]
            s = 12 - 7 + 5
            s = 10 
            '''
            s = s- code[(i + 1) %n] + code [(i + 1+ k) %n]
            print(s)
    if k < 0:

        s = sum(code[k : ])

        for i in range(n):
            sums[i] = s
            s = s + code[i %n] - code[(i + 1) %n]
    return sums

decrypt( code = [5,7,1,4], k = 3)
