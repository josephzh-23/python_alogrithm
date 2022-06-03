from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque()

    # will add to the right side of the queue
    # if you add 1, then 2, 2 will be ahead of 1
    def push(s, x:int):
        s.q.append(x)

    # last in first out
    # from 3  4  5
    # becomes 5 4 3     as shown above
    def pop(s):
        for i in range(len(s.q) -1):
            s.push(s.q.popleft())
        return s.q.popleft()

    def top(s):
        return s.q[-1]

    def empty(s):
        return len(s.q)==0


s = MyStack()
s.push(3)
s.push(4)
s.push(5)
print(s.pop())
