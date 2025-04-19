'''



[2,1 ,5, 6, 2, 3]
Also keep track of the max area that's also very important here
Keep a monotoinc stack increasing

stack
i = 0
index  height
0      2

i = 1
1 < 2
Then pop 2 after see 1
index  height
0      1

Then we see 5 and 6 everythign is fine
index  height
0      1
2      5
3      6

Then we see 2, start popping again
0   1
2   2

Then see 5
0   1
2   2
5   3
'''
from typing import List


def largestRetangleArea(heights:List[int])-> int:
    maxArea = 0
    stack = []

    for i, h in enumerate(heights):
        start = i
        '''
        When we need to pop here 
        '''
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            print("index and height", index, height, i)
            '''
            when i = 4 
            [2, 5] 
            (4 - 2)  * 5 =  10 
            
            The above gives us here 10 
            '''
            maxArea = max(maxArea, height * (i - index))
            start =index
        stack.append((start, h))
    print("stack here is with max area" , stack, maxArea)

    '''
    
    This is to process what's left here in the states here 
    and then return the max area here 
    [(0, 1), (2, 2), (5, 3)]        and then here we have the code 
    len(heights) = 6 
    h = 3
    This is what's left in the stack here 
    and then we need to calculated the area fom these heights here 
    '''
    for i ,h in stack:
        maxArea = max(maxArea, h * len(heights) -i)
    return maxArea

heights = [2,1,5,6,2,3]
print(largestRetangleArea(heights))





















