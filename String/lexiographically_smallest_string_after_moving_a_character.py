def answer(s):
    '''
    For each chacater


    For each character, remove it from its current position and try placing it at every possible new position in the string.
For each new string formed, check if it's lexicographically smaller than the previous smallest string


    Say 'cba'
    Remove 'c' from the start and try placing it in positions: ['cba', 'bca', 'abc'].
Smallest lexicographically is "abc".
    '''
    for i in range(len(s)):
        for j in range(len(s)):
            

answer("bdca")