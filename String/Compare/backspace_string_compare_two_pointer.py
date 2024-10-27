



'''

And then we have the code right here
'''
def backstringCompare(s, t)-> bool:
    def nextValidChar(str, index):

        backspace = 0
        while index >= 0:
            if backspace == 0 and str[index] != '#':
                break
            elif str[index] == "#":
                backspace +=1
            else:
                backspace -=1
            index-=1
        return index

    indexs, indext = len(s) -1, len(t) -1

    while indexs >= 0 or indext >= 0:
        indexs = nextValidChar(s, indexs)
        indext = nextValidChar(t, indext)

        chars = s[indexs] if indexs >=0 else ""
        chart = t[indext] if indext >= 0 else ""

        if chars != chart:
            return False

        indexs -=1
        indext -=1

        #the above is the solutino that we came up with here and this is very good here

    return True
