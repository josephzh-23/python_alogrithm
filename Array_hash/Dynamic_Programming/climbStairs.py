
'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

# of stairs                            0  1  2  3  4   5
# of ways to climb stairs              8  5  3  2  1   1
'''

def climbStairs(n):

    one, two = 1, 1

    for i in range(n-1):
        temp = one
        one = one + two

        # need to shift # 2
        two = one

    return one

steps = climbStairs(2)
print(steps)