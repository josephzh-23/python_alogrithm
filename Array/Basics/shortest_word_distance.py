'''

This is one of the code here
'''

def sol(words, word1, word2):


    length= len(words)
    res= 1000
    for i in range(length):
        print(i)

        if words[i]== word1:
            for j in range(0 , length):
                if words[j] == word2:
                    print(j, i)
                    res = min(res, abs(j- i))

    print(res)
wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
sol(wordsDict, word1, word2)