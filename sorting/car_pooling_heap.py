import heapq


class Solution(object):
    def carPooling(self, trips, capacity):

        minHeap = [] # pair of [end, numPassengers]

        curPass = 0
        for t in trips:

            numPass, start, end = t

            '''
            
            minHeap[0][0] is the end value of the last one 
            This means that the current trip added to the heap 
            has been completed 
            In case [[2, 1, 5] , [3, 3, 7]] 
            After [2, 1, 5] is processed, at i = 1 
            if minHeap[0][0] = 1 
            start = 5
            
            curPass -= 2 
            '''
            while minHeap and minHeap[0][0] <= start:
                # decrement this by the # of passengers here
                curPass -= minHeap[0][1]
                heapq.heappop(minHeap)

            curPass+= numPass
            if curPass > capacity:
                return False
            heapq.heappush(minHeap, [end, numPass])