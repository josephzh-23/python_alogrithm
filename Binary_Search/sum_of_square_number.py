'''
And then the probelm here quite different as said


'''
from math import sqrt


def judgeSquareSum(self, target: int) -> bool:
    # Initialize two pointers. `left` starts at 0, and `right` starts at the square root of target,
    # truncated to an integer, which is the largest possible value for a or b if a^2 + b^2 == target.
    left, right = 0, int(sqrt(target))

    # Loop until the two pointers meet
    while left <= right:
        # Calculate the sum of squares of the two pointers
        current_sum = left ** 2 + right ** 2


        if current_sum== target:
            return True

        elif current_sum < target:
            left +=1
        else:
            right -=1
    return False
