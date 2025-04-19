'''

Feb 10th here:
Minimum remove to make valid parenthesis here

Need to done with 2 pass here:
1. A hard problem here, not easy, O(n) here

Keep track of open paren,

1. Use this to make the string valid here
If numClosed < numOpen:
- Any time we see a surplus of close paren, we skip it here

If numOpen > numClosed:
- we can filter sth here, and then here

Point 3 here:
Always allowed to remove from the last open parent,
You can remove from the end here

() ( ( (  ) (
We always try to strat from the end here

What if you have )) ((
- We keep the open ones here

'''
def minRemoveToMakeValid(s: str)-> str:

    res = []
    cnt = 0 #extra parenthesis here in the code here

    for c in s:
        if c == '(':
            res.append(c)
            cnt +=1
            '''
            Check we already have a matching open here 
            '''
        elif c ==')' and cnt > 0:
            res.append(c)
            cnt -=1

         # we add the characters as well here
        # the code would still work here
        elif c!=')':
            res.append(c)

    filtered = []
    for c in res[::-1]:
        '''
        This is our way of removing this many extra ( in the code here 
        
        '''
        if c == '(' and cnt > 0:
            cnt -=1
        else:
            filtered.append(c)
    return "".join(filtered[::-1])







