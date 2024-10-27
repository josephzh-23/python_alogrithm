'''


This is using approach 3 here with suffix array with sorting here
1. And this is important here
2. 2
'''


def longestRepeatingSubstring(s: str) -> int:
    length = len(s)
    suffixes = []

    # Create suffix array by storing all suffixes of the string
    for i in range(length):
        suffixes.append(s[i:])
    # Sort the suffix array
    suffixes.sort()

    max_length = 0
    print("suffixes are", suffixes)
    '''
   ['a', 'aba', 'abbaba', 'ba', 'baba', 'bbaba']
   
   The suffixes 
    
    '''
    # Compare adjacent suffixes to find the longest common prefix
    for i in range(1, length):
        j = 0

        # Compare characters one by one until
        # they differ or end of one suffix is reached

        '''
      'aba'     0 < 3
      'a'   0 < 1 
      j here would be 
      and j is the pointer that compares char by char between "aba" and "a"
      
      j would be put at the maximum of whichever here or there 
          '''
        while (j < min(len(suffixes[i]), len(suffixes[i - 1])) and suffixes[i][j] == suffixes[i - 1][j]):
            j += 1

        # Update max_length with the length of the common prefix
        max_length = max(max_length, j)
    return max_length


s = "abbaba"
longestRepeatingSubstring("abbaba")
