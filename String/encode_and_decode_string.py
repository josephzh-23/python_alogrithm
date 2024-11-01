'''


'''

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.

    What we want if given "neet" how to know where to start and where to end?
    well
    for "neet" ->  "4#neet"
    for "neetcode" ->  "4#neet5#co#de"

    TC: O(n) here
    """

    def encode(self, strs):
        res = ""
        for s in strs:
            # add the number, the delimiter and the letter itself
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1

            #Tell us how many length we would have to read to get to the character string.
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res