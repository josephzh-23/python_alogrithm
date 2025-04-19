'''

1. Goal

need to find a left and rigth pointer
Exactly the same as largest rectangele in historam problem here
1. Can pratice again here to get a better feel for things
2.

While stack[-1] and h <= stack[-1]
    stack.pop()
    # have found a right boundary here

2. For each index we pop from the stack, we use it
 to set the corresponding right bound for that bar to the current index (i), since we now know this bar is taller than the current bar h.


3. f there are still elements left in the stack after popping,

 it indicates that the current bar h > stack[-1]. Hence,
 the left boundary for the current bar h is now known to be the index on top of the stack.

 Let's go through an examle here
 [2, 1, 5, 6, 2, 3]


'''

def maxRectangle(matrix):