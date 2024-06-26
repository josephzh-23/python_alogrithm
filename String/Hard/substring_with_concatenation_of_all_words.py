"""
A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab"
are all concatenated strings. "acdbef" not a concacted substring b/c it's not the concatenation of any permutation of words
before

Return the starting indices of each word


The youtube video for this change here
https://www.youtube.com/watch?v=Bbu4Qjzf7A0&t=917s
s = "barfoothefoobarman"
words = ["foo", "bar"]

TC: O(n)        words words to match against here
"""

def ans(string, words):

    if(string is None or len(string) == 0 or words is None or len(words) == 0):
        return []

    freqMap = {}
    for word in words:
        freqMap[word] = 1 + freqMap.get(word, 0)


    eachWordLength = len(words[0])
    # the total word legnth would be like "abcde" -> 5
    totalWords = len(words)

    res = []
    # only have to go up to that far here
    for i in range(0, len(string) - totalWords * eachWordLength + 1):

        seenWords = {}

        # would be 2 words each time at all time
        for j in range(0, totalWords):
            '''
        eachWordLength always 3 here 
        but wordIndex = 0, 3,    1, 4       2, 5 order, increase by 3 each time
            '''
            wordIndex = i + j* eachWordLength
            print("word index is ", wordIndex, eachWordLength)
            word = string[wordIndex:wordIndex + eachWordLength]

            print("word is", word)

            # have not found the word
            if(word not in freqMap):
                break
            seenWords[word] = seenWords.get(word, 0) + 1

            # we have seen the words more than frequency map
            if(seenWords[word] > freqMap.get(word, 0)):
                break

            if(j + 1 == totalWords):
                res.append(i)

    print(res)
ans("barfoothefoobarman", ["foo", "bar"])


















