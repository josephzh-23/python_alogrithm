'''

Similar to longest valid parenthesis

(( )

) () () )

st =  ( (
    )
'''

def longestValidOrder(s):
    st = []
    c = 0
    for c in s:
        if c=='(':
            st.append(c)
        elif c == ')':
            if st[-1] == '(':
                st.pop()
                c+=1

    return c

