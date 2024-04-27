import heapq

h = heapq
def isSValid(str):

    freq ={}
    isValid = False
    #
    maxh = []
    h.heapify(maxh)

    for c in str:
        if c not in freq:
            freq[c] = 1
            #already in there
        else:
            freq[c] += 1

    # get the min char occurence
    # and start putting in with teh count
    for char, count in freq.items():

        h.heappush(maxh, [-count, char])

    count, char = h.heappop(maxh)
    print(count, char)
    count, char = h.heappop(maxh)
    print(count, char)

    # get the min # of occurence of item this would help


isSValid("jjjoseeph")

    # case 2    check if you can remove 1 char
    # cover this case by case then
    #abcc




    # all char appear same # of times

    # rmv 1 char at 1 indx in the string ,
    # remaining char occur same # of times
