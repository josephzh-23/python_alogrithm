
# check if 1 string is a substring of another

# use 1 call to this is the dumb approach
# ex: waterBottle a rotation of "erbottlewat"

# Note this is diff from palindrome as noted,


# O (n *n )
# solution 1:
def isRotation(s1, s2):
    n1 = len(s1)
    n2 = len(s2)

    if n1 != n2:
        return False

    # Create a temp string with value str1.str1
    temp = s1 + s1

    # Check if str 2 is a substring of temp
    if temp.count(s2) >0:
        return True
    else:
        return False

# Driver program to test the above function
string1 = "AACD"
string2 = "ACDA"

if isRotation(string1, string2):
    print("Strings are rotations of each other")
else:
    print("Strings are not rotations of each other")


# Solution 2: A better solution here