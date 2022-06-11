

def containsDuplicateMethod1(nums):

    hash = set()

    for num in nums:
        if num not in hash:
            hash.add(num)
        else:
            return True
    return False

# check if it contains duplicate
def containsDuplicateMethod2(nums):

    hash = {}

    for num in nums:
        if num not in hash.keys():

            hash[num] = 1
        else:
            hash[num] +=1
            for key, val in hash.items():
                print('the value is ',key , '', val)
            return True


    return False

# writing the duplicate
arr = [1, 2, 3, 4,5,5]
print('duplicate is', containsDuplicate(arr))

