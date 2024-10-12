'''


Using the code here, you then have

sqrt(x) = 2 * sqrt(x/ 4)


mySqrt(x) = mySqrt(x >> 2) << 1



Suqre root here can actually be done with recursion here

Here the probelm can be done with recursion here

Base case sqrt(x) = x for x < 2
'''



def mySqrt(x):

    if x<  2:
        return x

    '''
    The above solutino here would work here 
    '''
    left = mySqrt(x >> 2) << 1
    right = left + 1
    return left if right * right > x else right


mySqrt(8)