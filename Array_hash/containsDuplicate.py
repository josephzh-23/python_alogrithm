'''

Using set here
1. go thru string
2.
'''
def containsDuplicateMethod1(nums):

    hash = set()

    for num in nums:
        if num not in hash:
            hash.add(num)
        else:
            return True
    return False



