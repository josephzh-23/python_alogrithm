
class MovingAverage(object):

    def __init__(s, size):
        """
        :type size: int
        """
        s.size = size
        s.arr = [0] * size

    def next(s, val):
        """
        :type val: int
        :rtype: float
        """
        if len(s.arr) >= s.size:
            del s.arr[0]
            s.arr.append(val)

c = MovingAverage(3)
c.next(1)
print(c.arr)

c.next(2)
print(c.arr)

c.next(4)
c.next(10)
print(c.arr)