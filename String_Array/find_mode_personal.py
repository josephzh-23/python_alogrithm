def findModeInArray(arr):
    # given an array then find the mode (the one that appears most)

    mode = []

    freq = {}

    for c in arr:
        if c not in freq:
            freq[c] = 1
            #already in there
        else:
            freq[c] += 1

    # loop thru freq, find the keep a max
    max = 0
    for key, val in freq.items():

        # max = 0 , val = 5
        print('value is ', key, val)
        if val > max:
            mode.clear()
            mode.append(val)
            # need to update the max here
        if max <= val:
            max = val
    return mode

result = findModeInArray("josephhhh")
print(result)