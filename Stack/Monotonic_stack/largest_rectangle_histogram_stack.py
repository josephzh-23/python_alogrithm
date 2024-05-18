'''
This is the one from the code here

Use stack to store the indexes as sadi before

1. Initialize an Empty Stack: This stack will store indices, not the actual heights.
2. Iterate Over the Histogram: For each bar, do the following:

3. While the stack is not empty and the
current bar’s height <  height at the stack’s top index, pop the stack.

4.
For each popped index, calculate the area. The height[popped_index]
 The width is the difference between the current index and the new stack’s top index minus one.
Push the current index onto the stack.

5. And then part 5 here also important

Handle Remaining Bars: After processing all bars, there might still be some indices left in the stack. For each
remaining index, the height is the height of the bar at that index,
 and the width is the difference between the
length of the histogram and the stack’s top index minus one. '''
