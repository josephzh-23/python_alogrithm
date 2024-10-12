class Solution:

    '''

Let's go back to the interview context. For x≥2 the square root is always smaller than x/2 and larger than 0 :
0<a<x/2.

Since a is an integer, the problem goes down to the iteration over the sorted set of integer numbers.
Here the binary search enters the scene.

    '''
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot

        return right