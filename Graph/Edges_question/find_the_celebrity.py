

g = [[1, 1, 0], [0, 1, 0], [1, 1, 1]]

print(g[0])

'''
Base case: i = 0, j = 1. We check knows(0, 1) and determine a potential candidate.
If knows(0, 1) = 1, j is the potential candidate.
If knows(0, 1) = 0, i is potentnial candidate here 

2. After determining a candidate between 0 and 1, we need to compare the winning candidate
 with a 3rd number. 
Therefore, we need a for loop to always go to the next number so that the candidate can compare to. 

3. 
Could be a celebrity 
If knows(candidate, j) == 1 we eliminate the current candidate and set `candidate = j`.

May not be a celebrity here 
If knows(candidate, j) == 0 we eliminate j=1 and keep the current candidate.
'''






