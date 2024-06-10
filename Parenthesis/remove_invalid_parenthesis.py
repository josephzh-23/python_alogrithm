

''''''
'''
Remove the smallest number here to make the string a valid expression.

lCount: increment the left count (l) when we encounter an opening parenthesis.


With these counts: use dfs to traverse the string and try the following:
Still have left parenthesis to remove (l > 0)


l: the count of left parentheses that we can still remove.
r: the count of right parentheses that we can still remove.
lCount: # of left paren that need to be removed
rCount: # of right paren that can be removed
t: current state of string after removals


When i == len(s):
    - check if both l and r = 0 here
    - add cur string t to the set ans here

Determining Parentheses to Remove: We begin by iterating through the string s and counting the number of invalid left ( and right ) parentheses.
Start with l = r = 0.

For each character in s:
case1:
If (, increment l to indicate we have another left parenthesis that can be balanced later.
    as l = # of l that need to be removed

case 2:
If ) and l > 0, it means there's a left parenthesis that can balance it, so we decrement l.

case 3:
If ) and l == 0, there is no left parenthesis to balance it, so we increment r, no left parenthesis

Setting up for dfs:

1. Go back and remove things, once at the end does left == right count? If yes, then yes otherwise no
2. if l == r, then look at lenght of string here

3. line 21: take or not to take


Step 2 : set up for dfs:


'''

'''
# line 32: why can't we take right parent greedily? because if we have sth like the above

#  (() ) ) (((
         *
         The one above here will not take eventually here, 
         
         lcount > rcount    so we can close it here otherwise we can't 
         
         36: english letter take all of the letters here 
         
         curres.append(curres)
         # take it and then dfs your way through here 
         
         #
         '''