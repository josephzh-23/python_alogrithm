'''

Here the solution then becomes


Build a for loop here,

'''


def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    # Initialize count of subarrays, product of elements, and the start index
    count_subarrays = 0
    product = 1
    start_index = 0

    # Iterate over the list using index and value
    for end_index, value in enumerate(nums):
        product *= value  # Update the product with the current value
        '''
        This is where the shriking would happen here 
         When the product is equal or greater than k, divide it by the
         starting value and increment the start_index to reduce the window size
         
         '''
        while start_index <= end_index and product >= k:
            product //= nums[start_index]
            start_index += 1

        # Calculate the new subarrays with the current element

        # and then using the code here w # and that's why i was able to keep the code a
        # Here, (end_index - start_index + 1) gives the count of subarrays ending with nums[end_index]
        count_subarrays += end_index - start_index + 1

    # The final result is the count of subarrays satisfying the condition
    return count_subarrays
