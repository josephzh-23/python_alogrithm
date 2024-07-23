'''
Manages reservation here


'''
from Heap.max_heap import MinHeap


class SeatManager(object):

    def __init__(s, n):

        s.unreserved = MinHeap()
        s.reserved  =[]
        for i in range(1, n):
            s.unreserved.push(i)
        """
        :type n: int
        """
    # smallest number unreserved seat here, reserve and then return here
    def reserve(s):
        """
        :rtype: int

        This much is clear here
        """

        unreserved = s.unreserved.pop()
        s.reserved.append(unreserved)
        print(unreserved)
        return unreserved


    #
    def unreserve(s, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        s.unreserved.push(seatNumber)
        if seatNumber in s.reserved:
            s.reserved.remove(seatNumber)

n =5
seatNumber = 2
obj = SeatManager(n)
param_1 = obj.reserve()
param_1 = obj.reserve()
# obj.unreserve(seatNumber)