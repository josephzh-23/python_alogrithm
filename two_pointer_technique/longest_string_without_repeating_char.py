

'''
Video by Michael Muniko's

Look at this example

 P W W K E W W
           i
     j
 max = 3
 set = [ w k e ]

 Now we see w
 next iteration: since w is already here, remove it

  P W W K E W W
              i
        j
 max = 3
 set = [ k  e  w]
 this way you can add w again


'''
# Also done from coding simplfied
def longestStringWithNoRepeatingCharacters(input):

    if not input or len(input)==0:
        return 0

    #always move i forward, prime pter
    i, j = 0

    # We will move the j pointer forward when a duplicate is found,
    # otherwise keep the same
    maximum = 0

    # Using set is easier than dictionary
    set1 = set()


    while i < len(input):
        char = input[i]

        # This means that a duplicate is encountered 
        # by having this first before adding to set, make sure to mve j forward
        # with >1 duplicate found
        while char in set1:
            set1.remove(input[j])
            j+=1

        # And then add to set
        set1.add(char)

        # Compare max with maximum sliding window
        maximum =max(maximum, i-j+1)
        i+=1
    return maximum




longestStrignNum = longestStringWithNoRepeatingCharacters("jfsdooooooosephfrt")
print(longestStrignNum)