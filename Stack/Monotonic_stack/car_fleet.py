

'''




t = (target - position[i]) / speed[i]

We compare this time with the time of the previously considered car (starting from the closest to the target).
If t > pre (previous car's time), will not catch up here

Repeated until have consired all cars
The total number of fleets (ans) is the answer we are looking for.


'''
from typing import List


def carFleet( target: int, position: List[int], speed: List[int]) -> int:
    size = len(position)
    time_position_speed = [0] * size

    for i in range(size):
        time = (target - position[i]) / speed[i]
        time_position_speed[i] = [time, position[i], speed[i]]

    time_position_speed.sort(key=lambda x: x[1], reverse=True)

    fleet = 1
    curr_idx = 0

    print(time_position_speed)
    for i in range(size):

        # if time taken greater
        if time_position_speed[i][0] > time_position_speed[curr_idx][0]:
            fleet += 1
            curr_idx = i
    return fleet

target = 12 ;
position = [10,8,0,5,3];
speed = [2,4,1,1,3]
print(carFleet(target, position, speed))








