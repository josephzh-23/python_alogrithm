'''
And then here we have the code as above here

And then we have the code


For the algorithm that we have we use

Addition: nums[-2] += nums[-1]
Subtraction: nums[-2] -= nums[-1]
Multiplication: nums[-2] *= nums[-1]
Division: nums[-2] = int(nums[-2] / nums[-1])

'''
from typing import List


'''
And the abov

'''

def evalRPN(tokens: List[str]) -> int:
    # Stack for storing numbers
    number_stack = []

    # Loop over each token in the input list
    for token in tokens:
        # If the token represents a number (accounting for negative numbers)
        if len(token) > 1 or token.isdigit():
            # Convert the token to an integer and push it onto the stack
            number_stack.append(int(token))
        else:
            # Perform the operation based on the operator
            if token == "+":
                # Pop the last two numbers, add them, and push the result back
                number_stack[-2] += number_stack[-1]
            elif token == "-":
                # Pop the last two numbers, subtract the second from the first, and push back
                number_stack[-2] -= number_stack[-1]
            elif token == "*":
                # Pop the last two numbers, multiply, and push the result back
                number_stack[-2] *= number_stack[-1]
            else:  # Division
                # Ensure integer division for negative numbers too
                number_stack[-2] = int(float(number_stack[-2]) / number_stack[-1])
            '''
            Pop the last element from the stack here and then that's good here 
        
        Basically the way this thing works is that the first time this pops here we get
        ["2","1","+","3","*"]
        
        
    1st:
        b/c 2 + 1 = 3
        and then first time we have [3, 1] 
        pop 1 
        [3] 
        
    2nd:
        3 * 3= 9 
        [9, 3]  then pop the 3 
        you get 9 here and then the above would work perfectly here  interesting 
            
            '''
            print("stack is", number_stack)
            # Pop the last number (second operand) from the stack as it's been used
            ans = number_stack.pop()
            print("the answer is", ans)
    # Return the result which is the only number left in the stack
    return number_stack[0]


'''
And above is the solution that we are looking for here 

'''
print(evalRPN(["2","1","+","3","*"]))