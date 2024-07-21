'''
WIth left start, then do sth starting here,
increment the right count here,

if left == right, then done here,
if not, then go to the part from l to r,

if l > r,

Iter thru everything once front and then once backwards here

'''

def minRemoveToMakeValidParenthesis(s)-> str:

'''
1. Use a stack here

- track indexes of the unmatched "(",

2. Use a set to
keep track of the unmatched ")"

3.
'''


def minRemoveToMakeValid(self, s: str) -> str:
    indexes_to_remove = set()


    '''
    
    If we put the indexes of the "(" on the stack,
     then we'll know that all the indexes on the stack at the end are the indexes of the unmatched "("
    '''
    stack = []
    for i, c in enumerate(s):
        if c not in "()":
            continue
        if c == "(":
            stack.append(i)


        # the stack not empty
        elif not stack:
            indexes_to_remove.add(i)

        # we see a ) here pop the ( to match it
        else:
            stack.pop()
    indexes_to_remove = indexes_to_remove.union(set(stack))
    string_builder = []
    for i, c in enumerate(s):
        if i not in indexes_to_remove:
            string_builder.append(c)
    return "".join(string_builder)