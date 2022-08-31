


def checkForDuplicateInArray(arr):

    #how to check for duplicates
    dup = set()
    freq = {}

    for c in arr:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] +=1
            dup.add(c)

    return dup

arr = [1, 2, 3, 4, 4, 5]
res = checkForDuplicateInArray(arr)

print(res)