'''

So we need to set the left and the right like the following:

, we set the left boundary as left = 1 since it is the minimum possible valid time,
 we also set the right boundary as right = totalTrips *maximum_time where
 maximum_time equals the maximum time taken by one trip, s



times[i] : time taken by ith bus to complete 1 trip here
times = [1, 2, 3]
Return the minimum time required for all buses to complete at least totalTrips trips.

times[0] = 1
takes 1 hour to complete 1 trip

'''
import math


def minimumTime(self, time, totalTrips):
    l, r = 0, max(time) * totalTrips
    #wanna return the minimum time required

    while l <= r:
        mid = (l + r) // 2
        if timeEnough(mid, time, totalTrips):
            r = mid
        # greater than the h given
        else:
            l = mid + 1
    return l


# # Can these buses finish 'totalTrips' of trips in 'given_time'? and this is intersting
def timeEnough(given_time, times, totalTrips):
    actual_trips = 0
    for t in times:
        actual_trips += given_time // t
    return actual_trips >= totalTrips