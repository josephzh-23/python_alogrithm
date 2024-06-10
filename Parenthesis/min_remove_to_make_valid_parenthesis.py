'''
WIth left start, then do sth starting here,
increment the right count here,

if left == right, then done here,
if not, then go to the part from l to r,

if l > r,

Iter thru everything once front and then once backwards here

'''

def minRemoveToMakeValidParenthesis(s)-> str:

    lcount = rcount = 0
    str =[]

    for c in s:
        if c == "(":
            lcount +=1
            str.append(c)


        elif c == ")":
            if lcount > rcount:
                rcount +=1
                str.append(c)
        else:
            str.append(c)

    # so this is step #1 here $ and then

    if lcount == rcount:
        return "".join(str)



    #this is good so here we are going from the back to account for the the (
    # and anything else like that
    else:
        res = []
        for i in range(len(str) -1, -1, -1):
            c = str[i]

            if c == "(":
                if lcount <= rcount:
                    res.append(c)

                else:
                    lcount +=1
            elif c == ")":
                res.append(c)
            else:
                res.append(c)

            # and then here we are done
            return "".join(reversed(res))


