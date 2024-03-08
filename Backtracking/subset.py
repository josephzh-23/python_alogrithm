

# Using the python way to do this much more readable



def subset(nums):
    resList = []
    tempSet = []
    backtrack(resList,tempSet , nums, 0)
    print(resList)
    return resList

def backtrack(resList, tempSet, nums, start):

    resList.append(tempSet.copy())
    for i in range(start, len(nums)):

        # case where including the number
        tempSet.append(nums[i])

        # if include then keep going
        backtrack(resList, tempSet, nums, i + 1)
        # case not including the number
        tempSet.pop()

arr = [1, 2, 3]
subset(arr)