# Python3 program of Next Greater Frequency Element

mystack = []
mymap = {}

"""NFG function to find the next greater frequency
element for each element and for placing it in the
resultant array """


def NGF(arr, res):
    n = len(arr)

    # Initially store the frequencies of all elements
    # in a hashmap
    for i in range(n):
        if arr[i] in mymap:
            mymap[arr[i]] += 1
        else:
            mymap[arr[i]] = 1

    # Get the frequency of the last element
    curr_freq = mymap[arr[n - 1]]

    # push it to the stack
    mystack.append([arr[n - 1], curr_freq])

    # place -1 as next greater freq for the last
    # element as it does not have next greater.
    res[n - 1] = -1

    # iterate through array in reverse order
    for i in range(n - 2, -1, -1):
        curr_freq = mymap[arr[i]]

        """ If the frequency of the element which is
        pointed by the top of stack is greater
        than frequency of the current element
        then push the current position i in stack"""
        while len(mystack) > 0 and curr_freq >= mystack[-1][1]:
            mystack.pop()

        # If the stack is empty, place -1. If it is not empty
        # then we will have next higher freq element at the top of the stack.
        if (len(mystack) == 0):
            res[i] = -1
        else:
            res[i] = mystack[-1][0]

        # push the element at current position
        mystack.append([arr[i], mymap[arr[i]]])

    print(res)
arr = [1, 1, 1, 2, 2, 2, 2, 11, 3, 3]

res = [0] * (len(arr))
NGF(arr, res)
