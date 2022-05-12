

def longestStringWithNoRepeatingCharacters(input):

    if not input or len(input)==0:
        return 0

    #always move i forward, prime pter
    i=0

    # We will move the j pointer forward when a duplicate is found
    j= 0
    maximum = 0

    set1 = set()
    while i< len(input):
        c = input[i]

        # by having this first before adding to set, make sure to mve j forward
        # with >1 duplicate found
        while c in set1:
            set1.remove(input[j])
            j+=1

        # otherwise add to set
        set1.add(c)
        maximum =max(maximum, i-j+1)
        i+=1
    return maximum

longestStrignNum = longestStringWithNoRepeatingCharacters("jfsdooooooosephfrt")
print(longestStrignNum)