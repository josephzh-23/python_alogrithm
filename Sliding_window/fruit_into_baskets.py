from Util.increment import inc
from Util.increment import dec


def minSubArraySize(arr):
    # keep track of smallest subarray length
    sum, l, r, minLen = 0, 0, 0, float('inf')
    fruits = 0


    s = set()
    while (l < len(arr)):
        '''

        Here keep increasing the window if not true 
        if window's leading edge has NOT reached the end of the array
        AND window's values do NOT add up to num, grow window to right
        '''

        if r < len(arr) and len(s) <= 2:
            s.add(arr[r])

            r += 1
            fruits+=1
        # when the window no longer true shrink again here
        # by increasing the left pointer
        elif len(s) > 2:
            '''
            '''
            # decrease the sum by value at the window trailing edge here
            l += 1
            fruits-=1
            s.remove(arr[l])
        else:
            break
    print(fruits)
    # return 0 if minLen == float('inf') else minLen


# fruits = [1,2,1]
# fruits = [0, 1,2,2]
fruits = [1, 2, 3, 2, 2]
minSubArraySize(fruits)