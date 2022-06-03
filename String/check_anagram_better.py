


"""
To check if 2 strings are anagrams, use hashmap
- store [ character, # of char ]

T(n) = O(n) + O (n) + O(n) = O(n)
S(n) = O (n) + O (n)
"""

"""
 Use 2 dictionary approach 1 for frequency 1 and 1 for frequency 2 
"""

def areAnagrams(s1, s2):
    if len(s1) != len(s2):

        return False

    # This is for space complexity here
    # O (n) and O(n)
    freq1= {}
    freq2= {}

    # O(n)
    for ch in s1:
        if ch in freq1:
            freq1[ch] +=1
        else:
            freq1[ch] =1

    # O (n)
    for ch in s2:
        if ch in freq2:
            freq2[ch] +=1
        else:
            freq2[ch] =1

    # O (n)
    # Loop over #1
    for ch in freq1:
        print("the key value is ", ch)
        if ch not in freq2 or freq1[ch] != freq2[ch]:
            return False

    return True


areAnagrams("joe", "eoj")






