'''
three sum smaller binary search values here
'''


def threeSumBinarySearch(nums):
    nums.sort()

    s = set()

    for i in range(len(nums)):
        target = 0 - nums[i]
        binarySearch(nums, i, s, target)

    print(s)


def binarySearch(arr, i, s, target):
    l = 0; r = len(arr) - 1

    while l < r:
        sum = arr[l] + arr[r]

        if sum < target:
            l += 1
        if sum > target:
            r -= 1

        # the one where they are equal here and that's it here
        # this is very important here
        # and then that's the one that we wanted here
        else:
            if l != i and r != i:
                temp = [arr[i], arr[l], arr[r]];
                temp.sort()
                res = tuple(temp)

                s.add(res)
                print("the s here is ", s)
            l += 1;
            r -= 1


nums = [-1, 0, 1, 2, -1, -4]

'''

The answre then here becomes 
'''
threeSumBinarySearch(nums)
