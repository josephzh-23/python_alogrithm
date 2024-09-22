'''

How to work on this problem here

1. Need to normalize the string first here
2. And then 23 * 60 = 1380

3.

'''

def findMinDifference(timepoints)-> int:

    for i, time in enumerate(timepoints):

        hours, minutes = time.split(":")
        minPastNight = int(hours) * 60 + int(minutes)


        # here we normalize this first and then
        timepoints[i] = minPastNight


        '''
        Need to handle the case of the wrap around here
        - [0, 1439]
        
        - the difference is only 1 here 
        
        '''
    timepoints.sort()
    res = 1440 + timepoints[0] - timepoints[1]


    for i in range(1, len(timepoints)):
        res= min(res, timepoints- timepoints[i - 1])
    return res