'''

Given a random alpha-numeric string with no special characters,
reformat the string without adding or removing any characters so that
no alphabet characters are adjacent to any other alphabet characters


    and no numeric characters are adjacent to any other numeric characters,
if possible, and return the modified string.
If it is not possible to reformat the string in that way,

    then group all the alphabet characters at the beginning of the string and
all numeric characters at the end of the string. In either case keep all alphabet
characters in the same order relative to each other before and after the formatting
and also keep all numeric characters in the same order releative to each other before and after the formatting.

And the above is what you are looking for as said


'''

def stringManipulation(s):
    print(s)
    c = ""
    n = ""
    ans =""

    '''
    Rem is the answer that we had before here 
    
    '''
    rem = ""
    for i in range(0,len(s)):
        if s[i].isalpha():
            c = c+ s[i]
        else:
            n = n+ s[i]
    print("c and n are ", c,n)
    if len(c)==len(n) or (len(c)==len(n)+1) or (len(n)==len(c)+1):
        long = 0

    if len(c)<len(n):
        long = len(c)
        rem = n[len(c):]

    elif len(n)<len(c):
        long = len(n)
        rem = c[len(n):]
    elif len(c)==len(n):
        long = len(c)
    for i in range(0,long):
        ans = ans + c[i] + n[i]

    # we have to add the remaining length here
    if (len(c)>len(n)+1) or (len(n)>len(c)+1):
        ans = ans + rem


    print('answer is', ans)
stringManipulation("aabb12cc345")