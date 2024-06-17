

def reverseString(s):

    # do not return anything, just modify the s in place instead
    left = 0
    right = len(s) - 1

    while left< right:

        # then we just keep swapping
        temp = s[left]
        s[left] = s[right]
        s[right] = temp

        left +=1
        right -=1












