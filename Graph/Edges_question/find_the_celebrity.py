

g = [[1, 1, 0], [0, 1, 0], [1, 1, 1]]

print(g[0])

'''

Identify a possible celebritry among all people here 

Concepts:
1) if know(a, b) -> true, a is not celebrity 

The key here 
Every person other than the celebrity must know the celebrity, which means if knows(a, b) is true, a cannot be the celebrity.

2) The celebrity does not know anyone else, which implies if knows(a, b) is false,
 b cannot be the celebrity.
 celebrity 
 
2 loops:



Basic implementation:
1) first pass: idenitfy a celebrity candidate 
 

 Use for loop 
    from 1 to n:
        if know(ans, i):
            ans not celebrity 
            update celebrity to i (potential)
        elif !know(ans, i):
            ans could still be celebrity 
            


2nd pass: validating the candidate here 

1)  2nd for loop to verify that the candidate (held in the variable ans) is indeed the celeb

    if know(ans, i): false 
        disqualifies the canddiate 
        
2) every other person !know the candidate, we must ensure know(i, ans):
    basically everyone frmo i knows the ans here this !negotiated here 
    
3) This must be verified here and there is no way around it here 


'''


def findCelebrity(self, n: int) -> int:
    # Initialize the candidate for celebrity to 0
    candidate = 0
    # Iterate over the range from 1 to n-1
    for i in range(1, n):
        # If the candidate knows person i, then switch candidate to i
        if knows(candidate, i):
            candidate = i

    # Verify candidate is indeed a celebrity
    for i in range(n):
        # Make sure we skip comparing the candidate with themselves
        if candidate != i:
            # Candidate should not know anyone, and everyone should know the candidate
            if knows(candidate, i) or not knows(i, candidate):
                # If the condition fails, return -1 because there is no celebrity
                return -1

    # If all checks pass, return the candidate as the celebrity
    return candidate


# this lets you know whether A knows B and yadayadayada
def knows(personA, personB):
    '''
    Not yet done
    '''
