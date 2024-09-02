

'''
What we want is

a , b <= sqt(c)

'''


def bruteForce(n):
    sum = 0
    for i in range(n):
        sum += pow(i, 2)
        if sum == n:
            return True
        elif sum > n:
            return False


print(bruteForce(3))