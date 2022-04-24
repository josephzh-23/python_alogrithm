'''
we can presort in element uniqueness

- mode: an element that occurs the most

'''


def presortMode(arr):
    modeVal = 0
    n = len(arr)
    i = 0  # current run begins at position i
    modeFreq = 0  # highest frequency seen so far

    while i <= (n - 1):
        runlength = 1
        runValue = arr[i]

        while i + runlength <= n - 1 and arr[i + runlength] == runValue:
            runlength += 1

        # update the mode frequency
        if runlength > modeFreq:
            modeFreq = runlength
            modeVal = runValue

        i = i + runlength
    return modeVal


# driver test
arr = [1, 1, 2, 3, 4, 5, 5, 5]
mode = presortMode(arr)

print("the value is ", mode)
