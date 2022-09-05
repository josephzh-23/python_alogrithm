

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


TC: O (n) would be a linear time here
'''
# Get the java code from Michael munios
def longestSubstringWithNoRepeatingCharacters(arr):

    if not arr or len(arr)==0:
        return 0

    #always move i forward, prime pter
    i, j = 0, 0

    # We will move the j pointer forward when a duplicate is found,
    # otherwise keep the same
    maxim = 0

    #need to rework this using Niccki white's solutino is better
    dict = set()

    while i< len(arr):
        c = arr[i]
        while c in dict:
            dict.remove(c)
            j+=1
        dict.add(c)
        maxim = max(maxim, i-j+1)
        i+=1
    return maxim

longestStrignNum = longestSubstringWithNoRepeatingCharacters("abcabcbb")
print(longestStrignNum)

