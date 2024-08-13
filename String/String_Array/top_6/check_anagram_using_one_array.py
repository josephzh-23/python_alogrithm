
MAX_CHAR = 26



def areAnagrams(s1, s2):

    # build a list
    count = [0] * MAX_CHAR

    if (len(str1) != len(str2)):
        return False;

    for i in range(len(s1)):


        count[ord(s1[i]) - ord('a')] +=1
        count[ord(s2[i]) - ord('a')] -=1

    # See if there is any non-zero value in count array
    for i in range(MAX_CHAR):

        if(count[i] !=0):
            return False

    return True


# Driver code
str1 = "geeksforgeekss"
str2 = "forgeeksgeeksc"

# Function call
if (areAnagrams(str1, str2)):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")


