'''
And this is it here, the two problems here


An interesting problem here

The solutino here:

No problem
1.The solution first attempts to determine if the array is already sorted (c == len(nums) check).
If not, it identifies the first point where the order is violated (index).

2. It then tries to correct this violation by swapping the appropriate elements.
Finally, it checks if the array is now sorted after the potential swap.

'''

def check(nums) -> bool:

    #already sorted here

    for i in range(len(nums)):


            # this is where we begin the next thing2
            #then not sorted so return

    '''
  Basically the way this works is that if 
  nums[i] > nums[i + 1] more than once, we know it's not good then
  cause we can have several situations like that  
    '''
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            count +=1

        if count > 1:
            #then it's not good here
            return False
        # so this is part of the solution here and then that's good here
