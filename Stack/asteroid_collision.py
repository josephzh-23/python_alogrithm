'''

 a. If the `asteroid` is bigger than the asteroid on the top, then this asteroid on the top will explode, and we will pop it from the stack.

 b. If the `asteroid` has the same size as the asteroid on the top, then both will explode.
 Hence we will pop it from the stack; also, we will mark `flag` as `false` because this `asteroid` will also explode, and hence we won't save it into the stack.

 c. If the `asteroid` is smaller than the asteroid on the top, then the asteroid on the top will not explode,


 so we will not pop it. But the `asteroid` will explode and thus we will mark `flag` as `false`.

'''


def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    # Initialize a stack to keep track of asteroids that are still moving
    stack = []

    # Iterate through each asteroid in the list
    for asteroid in asteroids:


        # If asteroid is moving to the right (positive), push it to the stack
        if asteroid > 0:
            stack.append(asteroid)
        else:

            '''
            The case where we have 
            5 < -10 
            '''
            # While there is at least one asteroid in the stack moving to the right
            # and the current left-moving asteroid is larger (in absolute value)
            # than the top asteroid in the stack, pop the top of the stack
            while stack and stack[-1] > 0 and stack[-1] < -asteroid:
                stack.pop()

            '''
            
            5 == -5 
            '''
            # If the top of the stack is an asteroid with the same size as the
            # current one (but moving in the opposite direction), they both explode.
            if stack and stack[-1] == -asteroid:
                stack.pop()

                '''
                [-5], [10] this is a hard question  
                '''
            # If the stack is empty or the top asteroid is moving to the left,
            # push the current asteroid to the stack
            elif not stack or stack[-1] < 0:
                stack.append(asteroid)

    # Return the stack representing asteroids that survived the collisions
    return stack