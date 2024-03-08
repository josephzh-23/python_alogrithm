"""

The youtube video for this change here
https://www.youtube.com/watch?v=Bbu4Qjzf7A0&t=917s
s = "barfoothefoobarman"
words = ["foo", "bar"]

Done using a sliding window approach here
TC: O(m *n * length)   m words,
SC: O(m)
"""


def ans(string, words):
    if (string is None or len(string) == 0 or words is None or len(words) == 0):
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
        for j in range(totalWords):
            '''
        eachWordLength always 3 here 
        but wordIndex = 0, 3,    1, 4       2, 5 order, increase by 3 each time
        
        This tells us where the word will start each time here 
            '''
            startingIndex = i + j * eachWordLength
            print("word index is ", startingIndex, eachWordLength)
            word = string[startingIndex:startingIndex + eachWordLength]

            print("word is", word)

            # have not found the word
            if (word not in freqMap):
                break
            seenWords[word] = seenWords.get(word, 0) + 1

            # we have seen the words more than frequency map
            if (seenWords[word] > freqMap.get(word, 0)):
                break

            if (j + 1 == totalWords):
                res.append(i)

    print(res)


ans("barfoothefoobarman", ["foo", "bar"])
