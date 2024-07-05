'''
Repeated dna subsequence
Repeated dna

The k here would be 10 in any case?
2.
'''

# the length is 9 in this case here
def repeatedSubSequence(s):
    seen, res = set(), set()

    # iterate over all the substring of length 10 in the dna sequence:
    for l in range(len(seen) - 9):
        # window_sum = window_sum - arr[i] + arr[i + k]
        cur = s[l: l + 10]

        # this is the 2nd time we are seeing this here
        if cur in seen:
            res.add(cur)

            # we have seen this at least once here
        seen.add(cur)

    return list(res)














