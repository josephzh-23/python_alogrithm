


"""
Approach 1: bad apporach taking O(n)

"""


# this is used for unicode
NO_OF_CHARS = 256;



# use a dictionary in python

# Using approach 1:
# This is the bad approach, that takes O(n)

# Returns an array of size 256 containing count
# of characters in the passed char array
def getCharCountArray(word):
    count = [0] * NO_OF_CHARS;

    for char in word:
        count[ord(char)] += 1;
    return count

"abbc"
def firstNonRepeating(string):
    countArray = firstNonRepeating(string)
    index = -1
    k = 0

     # O(n) we go thru the string again just to check if it exists
    for char in string:
        if countArray[ord(char)] == 1:
            index = k
            break
        k += 1

    return index


"""
Approach 2: using dictionary to build this 

look up in hash map 
"""

def findFirstNonRepeatingChar(str):

    dict = {}

    size = len(str)

    # iterate thru string
    for i in range(size):
        key = str[i]

        # Check if key in dict
        if key not in dict:
            dict[key] = 1
        else:
            dict[key] = dict[key] + 1

    for key, value in dict.items():
        if value == 1:
            print("the key is", key ," and value is", value)
            break

findFirstNonRepeatingChar("jjosepdh")







