'''

why is 1 a possible answer?
for the points [-2, 1, 0]   distance 8?
| 1 - (-2) | *2 -> 6
| 1 - 1 | *2->  0
| 1 - (0) | *2 -> 2

6 + 2 <= 8 so this is ok

Find the lower bound in which it is true and then the upper bound
where it is true

The formula
n + d//2    here

if the bound is [-6, 4] then we check for the mid point first
and then do a bsearch on it, 

'''


def minimumTime(self, time, distance):
    l, r = 0, max(time) * distance
    #wanna return the minimum time required

    while l <= r:
        mid = (l + r) // 2
        if setup(mid, time) <= distance:
            r = mid
        # greater than the h given
        else:
            l = mid + 1
    return l

# if x = 0 then it's

# this is a suitable location here
def setup(mid, array):
    sum = 0
    for num in array:
        sum += 2 * abs(mid - num)

    return sum