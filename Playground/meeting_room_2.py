'''

The code here is also the sweep line algorithm here

'''
class Interval(object):
    def __init__(s, start, end):
        s.start = start
        s.end = end

def minMeetingRoom(intervals):

    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])

    print(start)
    res, count = 0, 0
    s, e= 0, 0
    while s < len(intervals):
        # [0, 3, 5]     [1, 2, 3]
        if start[s] < end[e]:
            s+=1
            count+=1
        else:
            e+=1
            count -=1

        res = max(res, count)
    return res


# using this we woudl have here
intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
minMeetingRoom(intervals)