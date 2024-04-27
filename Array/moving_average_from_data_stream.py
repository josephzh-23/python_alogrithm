'''
Calculate the moving avergage here

'''


class MovingAverage(object):

    def __init__(s, size):
        """
        :type size: int
        """
        s.avg = [0] * size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """


'''
So basically you are calling 
.next(1)
.next(10) 

'''