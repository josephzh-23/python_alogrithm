'''


Random pick index of the max value here

And that's step 1 here

Given an integer array nums of possible duplicates, randomly output an index of a max number found in the array here

! pick the same number twice here and to start off here we have the code here

And then that's the code here
'''

import random
def randomPickIndex_second_variant_398(nums):
    max_number = float('-inf')
    picked_index = -1
    n = 0
    for i in range(len(nums)):
        curr_num = nums[i]
        if curr_num < max_number:
            continue

        if curr_num > max_number:
            max_number = curr_num
            picked_index = i
            n = 1
        elif curr_num == max_number:
            n += 1
            r = random.randint(0, n - 1)
            if r == 0:
                picked_index = i
    return picked_index