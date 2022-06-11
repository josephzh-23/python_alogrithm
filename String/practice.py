

# using dictionary

def findFirstNonRepeating(arr):

    dict = {}

    for char in arr:
        if char not in dict.keys():
            dict[char] = 1
        else:
            dict[char] +=1

        # here wouldb e good
