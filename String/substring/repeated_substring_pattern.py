word = "abcabcabcabc"

# all appear the same times
def repeatedSubstringPattern(s):

    # divide this in 2 and then go
    length = len(s)

    for i in range(length//2):
        if(length % 2 == 0):
            numRepeat = length /i

            # get the substrign here
            substring = s[0: i]
            sb = ""
            for j in numRepeat:
                sb+=substring

            if sb==s: return True

    return False


repeatedSubstringPattern(word)