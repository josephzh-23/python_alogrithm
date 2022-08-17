
# Check if a string is a permutation of the other?

'''

2 strings are permutation of each other, then they would
have the same characters, but in diff orders, compare
the sorted version
'''


# TC: O(nlogn) if merge sort is used for both arrays
def arePermutation(str1, str2):
    # Get lengths of both strings
    n1 = len(str1)
    n2 = len(str2)

    # If length of both strings is not same,then automation is not the
    # same
    if (n1 != n2):
        return False

    # Sort both strings
    a = sorted(str1)
    str1 = "".join(a)
    b = sorted(str2)
    str2 = "".join(b)

    print(str1 , "and " , str2)
    
    # Compare sorted strings
    for i in range(n1):
        if (str1[i] != str2[i]):
            return False

    return True


# Driver Code
if __name__ == '__main__':
    str1 = "eoj"
    str2 = "joe"
    if (arePermutation(str1, str2)):
        print("Yes")
    else:
        print("No")

# This code is contributed by
# Sahil_Shelangia



