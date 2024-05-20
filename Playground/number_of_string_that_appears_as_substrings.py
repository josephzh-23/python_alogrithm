'''
# of strings that appears as substrigns here

very good question here

'''

def answer(patterns, word):
    c = 0
    for p in patterns:
        if p in word:
            c+=1

    print(c)
answer(['a', 'abc', 'bc', 'd'], 'abc')















