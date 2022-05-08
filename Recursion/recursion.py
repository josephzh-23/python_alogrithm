#The stack call will then return sth like
"""
Iteration 1         return "o"
Iteration 2         return "ol"
Iteration 3         return "oll"
Iteration 4         return "olle"
Iteration 5         return "olleh"
"""

# Check if string is empty or not in python
def reverseString(input):
    if len(input) ==0:
        return ""

    #else if recurse the substring



    return reverseString(input[1:]) + input[0]

    # product = reverseString(input[1:]) + input[0]
    # print(product)
    # return product

word = "joseph"
print(reverseString(word))