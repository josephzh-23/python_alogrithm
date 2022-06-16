'''
First of all, notice the below
a = [1]
b = [2]         the above will then be printed
c = a +b        print(C)  [1, 2]
'''

'''
Strategy:
input [ 1 2 3 ]     take 2 for example
[] + [2] = [2]
[1] + [2] = [1, 2]

'''
def subsets(nums):
    result = [[]]

    for num in nums:
        result += [i + [num] for i in result]
    return result

# notice in this case
