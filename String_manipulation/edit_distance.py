# useful for doing python related calculation here, can refer to the notes from before
# https://leetcode.com/problems/edit-distance/description/
def minDistance(word1, word2) -> int:
    """
    we have to make a 2d 1 row and 1 column bigger
    """
    cache = [[float("inf") * (len(word2) + 1)] for i in range(len(word1) + 1)]

    '''
    
    The following will start a 2d matrix based on the following 
        a  c    d
     a              3
     b              2
     d              1
        3  2    1   0          
    '''
    for j in range(len(word2) + 1):
        word1Length = len(word1)
        cache[word1Length][j] = len(word2) - j
    for i in range(len(word1) + 1):
        word2Length = len(word2)
        cache[i][word2Length] = len(word1) - i

    # bottom up dp approach
    # then we start from the back
    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if (word1[i] == word2[j]):
                cache[i][j] = cache[i + 1][j + 1]  # slowly come up that way
            else:
                cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])

    return int(cache[0][0])
