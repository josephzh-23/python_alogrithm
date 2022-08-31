def longestSubstringWithNoRepeatingCharacters(input):

# use 2 pter approach
    i, j = 0, 0

    maximum = 0
    # use a set
    dict = set()
    # abcda
    for c in input:
        if c not in dict:
            dict.add(c)

        else:
            # a duplicate found
            j+=1
            if i - j > maximum:
                print('here max is ', maximum)
                maximum = i - j
        i+=1

    return maximum

arr = "abcdeeeef"
res = longestSubstringWithNoRepeatingCharacters(arr)
print(res)