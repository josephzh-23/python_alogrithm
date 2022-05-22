
# practice from yesterday

def findFirstNonRepeatingChar(str):

# Given string "jooseph"
# can do this using dictionary
# Store val and frequency of seen
    dict = {}

    # after having tierated thru this
    for ch in str:
        if ch not in dict:
            dict[ch] = 1
            # alredy exists here
        else:
            dict[ch] +=1

    # loop thru dict and return the dict[val] = 1
    for value in dict.items():
        if value == 1:
            return value

val = findFirstNonRepeatingChar("joseee32")
print("the value is ", val)
