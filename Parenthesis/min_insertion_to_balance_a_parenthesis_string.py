'''
It's important to know how to do this here

Every open will have 2 consec closing brackets here
- ( ))

The processing:

Case 1
See a ) and there already is a (
"))" will cancel one "(". So if we have processed "(" and then ancountered ")" we need to see if we have another ")"
before deciding what to do.

check whether that is the only one ) here or there is 1 more ) after that here,

And that's the important part here

1. ans ++  ;   l --
'''

def minInsertions(s):
    l, ans, i = 0, 0, 0
    n = len(s)

    while i < n:
        c = s[i]

        # the one that needs to worry about here
        if c == ')':

            # the very next question here
            if i < n -1 and s[i+1] == ')':
                # move to the next pointer here
                i+=1
            else:
                ans+=1
            '''
            and also we need to decrement one left parenthesis 
            '''
            l-=1

            '''
            
             If in the process of decrementing left variable it becomes -1, that means that ")" was "dry" - without a matching "(", we need to
            '''
            if l < 0:
                l = 0
                ans+=1
        else:
            l+=1

        i+=1

        # as the final answer here
    return ans + 2 * l

def solution(s: str):
    l, r = 0, 0
    s = []
    '''
    
    ( ))        here then 
    
    '''
