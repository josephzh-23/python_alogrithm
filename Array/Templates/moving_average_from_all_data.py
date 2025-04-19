from collections import deque


'''
Initialization the initial size is 3 

and calling next moves to the next value 

'''


class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.curr_sum = 0

    def next(self, val: int) -> float:
        self.curr_sum += val
        self.queue.append(val)

        if len(self.queue) > self.size:
            self.curr_sum -= self.queue.popleft()

        return self.curr_sum / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)