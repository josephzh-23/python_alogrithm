def myPow( x: float, n: int) -> float:
    # Inner function to perform the quick exponentiation.
    # This reduces the number of multiplications needed.
    def quick_power(base: float, exponent: int) -> float:
        result = 1.0
        # Continue multiplying the base until the exponent is zero
        while exponent:
            # If exponent is odd, multiply the result by the base
            if exponent & 1:
                result *= base
            print('base is ',base)
            # Square the base (equivalent to base = pow(base, 2))
            base *= base
            # Right shift exponent by 1 (equivalent to dividing by 2)
            exponent >>= 1
        return result

    # If n is non-negative, call quick_power with x and n directly.
    # Otherwise, calculate the reciprocal of the positive power.
    return quick_power(x, n) if n >= 0 else 1 / quick_power(x, -n)


# so what you have to do here is basically
x = 2; n = 10
myPow(2, 10)