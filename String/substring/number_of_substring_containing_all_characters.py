

'''
Containing a, b and c here at least 1 occurence here
'''


# apply the sliding window with map solutino here

def numberOfSubstrings(self, s: str) -> int:
    ca = 0  # for count of a
    cb = 0  # for count of b
    cc = 0  # for count of c
    ans = 0  # count of total substring forming with 'a' and 'b' and 'c'
    j = 0  # index for moving forward in string s after at least 1 -> 'a','b','c' is found

    for i in range(len(s)):  # traversing in s
        if s[i] == 'a':  # 'a' found, store count
            ca += 1
        elif s[i] == 'b':  # 'b' found, store count
            cb += 1
        else:  # 'c' found, store count
            cc += 1

        while ca > 0 and cb > 0 and cc > 0:  # means at least 1 -> 'a','b','c' is found

            # this telling if the a,b,c is found then after appending remaining substring of s to this chosen
            # string (having at least 1 -> 'a','b','c') will all be VALID (means containing a,b,c in it)
            # BETTER DO IT IN PEN PAPER FOR BETTER UNDERSTANDING
            ans += len(s) - i

            # NOW THE WINDOW IS FORMED , ITS TIME TO MOVE THE INDEX FORWARD
            # AND CHECK IF FORWARD SUBSTRING CARRYING a,b,c or not -> will be checking from j
            # traversing in s after i

            # if s[j]=='a' or 'b' or 'c' found -> decrement the counts
            if s[j] == 'a':
                ca -= 1
            elif s[j] == 'b':
                cb -= 1
            else:
                cc -= 1
                # if any counts goes to 0, time to move the window (come out to this current while loop)

            j += 1  # move index

            if j == len(s):  # j reached to end of s
                return ans
    return ans
