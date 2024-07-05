#;;

'''

And then here we have the code

So basically try deleting a character here then start with this and
go where we take it

'''

def backstringCompare(s, t):
    finals = ''
    finalt = ''
    for c in s:
        if c == '#':
            # and then we have the code
            finals = finals[:-1]
        else:
            finals +=c
    for c in t:
        if c == '#':
            # and then we have the code
            finalt = finalt[:-1]
        else:
            finalt += c
    # and then this is the answer here? This would be a lot of fun here
    print(finals)
    print(finalt)
backstringCompare('ab#c', 'ad#c')