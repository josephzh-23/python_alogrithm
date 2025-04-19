'''

Using a stack for this problem here and how to do this here

And then using teh above we have the code here,

position: [10, 8, 0, 5]
speed: [2, 4, 1, 3]
target : 12 miles
'''
from collections import defaultdict



'''
1. 
What we do here is basically we have 
t = (target - position[i]) / speed[i]
get the time, 

2. 
If the calculated time t is greater than the time of the last car (or fleet) pre
current car will not catch up here 
if t > pre:
    ans += 1
    pre = t
    
    And that would be the above here and that's it here 

3. Remmeber only a new fleep is formed when 
there are different times and one catches to the other as said 
'''
def carFleet(target, positions, speeds):

    # combine the 2 arrrays first position and speeds
    pos_with_speeds = [list(x) for x in zip(positions, speeds)]
    pos_with_speeds.sort(key=lambda x: x[0])

    fleetCount = 0
    previous_time = 0
    for position, speed in pos_with_speeds[::-1]:
        print("position and speed are", position, speed)
        # Calculate the time needed for the current car to reach the target
        time_to_reach_target = (target - position)/speed
        # If this time is greater than the time of the previously counted fleet,
        # it means this car cannot catch up with that fleet and forms a new fleet.
        if time_to_reach_target > previous_time:
            fleetCount += 1  # Increment fleet count
            previous_time = time_to_reach_target  # Update the time of the last fleet



    # get the size of the # of times here
    print(fleetCount)

position= [10, 8, 0, 5]
speed= [2, 4, 1, 3]
target =12
carFleet(target, position , speed)

