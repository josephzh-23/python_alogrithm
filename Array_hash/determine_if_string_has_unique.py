# Python program to illustrate
# string with unique characters
# using data structure
MAX_CHAR = 256;


# string only has unique characters here

# TC: O(n)
def uniqueCharacters(array):
    n = len(array)

    # If length is greater than 256,
    # some characters must have
    # been repeated
    if n > MAX_CHAR:
        return False

    chars = [False] * MAX_CHAR

    #Basically use a flag i indicate whether string was seen before
    # if seen before then we return false immediately.
    for i in range(n):
        index = ord(array[i])

        '''
         * If the value is already True,
         string has duplicate characters,
         return False'''
        if (chars[index] == True):
            return False

        chars[index] = True
    return True


# Driver code
if __name__ == '__main__':

    input = "GeeksforGeeks"
    if (uniqueCharacters(input)):
        print("The String", input,
              "has all unique characters")
    else:
        print("The String", input,
              "has duplicate characters")

# This code is contributed by shikhasingrajput