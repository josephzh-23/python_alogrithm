'''
The current problem can be broken down into pow(x, n-1)
power (x, n) = x * power(x, n-1 )

But we don't want to do x ^n one by one, the problem is that that is too slow as you can see here (O (n))
1) We don't want sth too slow here

SO a better approach is when we have

If n is even
x ^n =  x ^2 *(n/2)


If n is odd
x * (x ^ 2) ^(n -1)/2

We reduce things by half here

2) And then what happens is that we try to take it down here by 1/2 and it becomes



'''


def binaryExp(self, x: float, n: int) -> float:
    # Base case, to stop recursive calls.
    if n == 0:
        return 1

    # Handle case where, n < 0.
    if n < 0:
        return 1.0 / self.binaryExp(x, -1 * n)

    # Perform Binary Exponentiation.
    # If 'n' is odd we perform Binary Exponentiation on 'n - 1' and multiply result with 'x'.
    if n % 2 == 1:
        return x * self.binaryExp(x * x, (n - 1) // 2)
    # Otherwise we calculate result by performing Binary Exponentiation on 'n'.
    else:
        return self.binaryExp(x * x, n // 2)


def myPow(self, x: float, n: int) -> float:
    return self.binaryExp(x, n)

