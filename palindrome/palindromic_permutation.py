'''
Using this question then we get the stuff that we wanted here

Using hashmap:
    Build a map with the character and then # of occurence of each character here

At end, traverse over the map here and the
    if count > 1 at any step,
        a palindromic permutation ! possible

    if count <2
         palindromic permutation is possible for string



'''
from collections import Counter


def canPermutateString(s):

    c = Counter(s)

    # can only be 1 model,we want to build an actual thing here
    count = 0
    for key in c.keys():
        count+= c[key] %2

    return count <= 1


print(canPermutateString("aab"))