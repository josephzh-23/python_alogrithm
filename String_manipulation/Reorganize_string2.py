from collections import Counter

from Heap import MaxHeap

'''



What's the question reorganize string here?

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

This is important here because no 2 words are the same
TC: O(nlogn)

Use a max heap-> b/c most frequent item here
1. this would mean O (logn)
2. can replace sorting for us

3. To use maxheap in python, replace count with -count
when pop min, actually poopping the max here

start with the most freq char
Use a hashmap
a -> 3      b -> 2     c -> 2

a: 3      a: 2      a: 1
b: 1 ->   b: 0  ->  b: 0
c: 1      c: 1      c: 0

Each time a letter is used, use a diff character
so use a previous to keep track of pointer


'''
def reorganizeString(s: str) ->str:

    # this will create a map with char: count
    # aaabbc
    # dict = {a: 3, b: 2, c: 1}
    count = Counter(s)
    mheap = MaxHeap()

    # use this instead of list comprehension

    for char, count in count.items():
        mheap.push([count, char])
    # store previous character we use so no reuse

    prev = None
    # add it to result
    res = ""

    while mheap or prev:
        if prev and not mheap:
            return ""

        # each time we want most freq char
        # except prev

        # count = the count -1 and then put it back in
        count, char = mheap.pop()
        res += char

        # instead of - because the whole thing is negative
        count -=1

        # already sth exists
        # this is after the count has already been descreased
        if prev:
            # [2, a]
            # h.heappush(mheap, prev)
            mheap.push(prev)
            prev = None

        # like we have already seen this now so don't add it here
        # if it's already 0, then we don't add anything here

        if count != 0:
            prev = [count, char]
    return res

s = "aab"
reorganizeString(s)