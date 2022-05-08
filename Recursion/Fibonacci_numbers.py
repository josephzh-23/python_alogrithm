"""
The Fibonacci number here:

    F (n) = F (n-1) + F(n-2)
    F0 = 0 and F1 = 1.

Approach 1: Recursion
Approach 2: Use dynamic programming

    input : n = 2
    output : 1
"""


def fibonaciNumberRec(n):
    if n ==1 or n==0:
        return n
    else:
        return fibonaciNumberRec(n - 1) + fibonaciNumberRec(n - 2)


print(fibonaciNumberRec(9))


#Approach 2 use dynamic programming here
"""
    We can avoid the repeated work done in method 1 
by storing the Fibonacci numbers calculated so far. 
"""