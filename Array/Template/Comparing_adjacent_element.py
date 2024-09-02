
nums = [1, 2,5, 4, 5]

# and then here we have the code

def checkIfSorted(nums):

    index= 0
    for i in range(len(nums) -1 ):

        # unsorted
        if nums[i] > nums[i +1]:
            index = i

    print(index)

checkIfSorted(nums)