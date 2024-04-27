class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """

        '''
 
 The idea here is to use 2 pointers and then have 1 for each field 
 
 
        '''


'''
The reason why this is better is because we still have to iterate over the words
O (n * k) -> this is inevitable 

but we save the string using the 2 pointer solution and now the SC is down to O (1) here and that's a lot better then before 

asdfsadfasasdfajkjkjnmnm
'''
def areTwoStringsEqual(word1, word2):
    # two pointers for the word
    w1 = w2 = 0
    # two pointers for each index here
    i = j = 0

    while w1 < len(word1) and w2 < len(word2):

        if word1[w1][i] != word2[w2][j]:
            return False

        # and then here we have the code

        # meaning they are the same
        i, j = i + 1, j + 1

        # and also need to reset each one when it gets to the
        # end so we have the code

        if i == len(word1[w1]):
            w1 += 1
            i = 0

    if j == len(word2[w2]):
        w2 += 1
        j = 0








