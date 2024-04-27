'''
And then using this we have the code
smaller subsmililar problem here where we have the code

power (x, n) = x * power(x, n-1 )


if x = 0, then x^n = 1  base case here

Basic idea :
(x ^2) ^ n/2    if even
x * (x ^2) (n-1)/2  if n is odd here

2 ^ 100 = (2 * 2 ) ^ 50
4 ^ 50 = (4 * 4) ^ 25       # up here as said and a lot more powerful above

# and then here the code should become

For the positive n, recursively copmuter half_pow as x ^ (n//2)
here as it's raised to the power of 1/2 here

n == even        recursively compute half_pow as x raised to the power (n // 2).

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

