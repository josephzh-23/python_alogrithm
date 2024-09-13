'''

Given an array of integers nums and an integer k. A continuous
subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

And then here we have the

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].


The thought process here:

Using a hashmap,
Based on these thoughts, we use a hashmap to store the prefix sum of indices as keys and their frequency of
occurrence as values.
Instead of modifying nums, we can apply the modulo 2 operation when storing values in the hashmap


1. identify sequences of elements within the array whose sum equals the number of odd elements needed to make a nice array.
2. And then here

we can calculate the sum of elements between two indices,

Between 2 start indices start and end, if # of odds between start and end == k,
found a nice subarray,

 current count (t in the code): # of odd numbers seen so far
t shows us how many times we have previously seen a count of t - k


Basically Now, if at an earlier point in the array we had encountered x - k odd numbers,
 any subarray starting from
that earlier point to our current position will have exactly k odd numbers. Why? Because x - (x - k) = k.


'''
from typing import List, Counter


def numberOfSubarrays( nums: List[int], k: int) -> int:
    # Initialize counter for odd counts with 0 count as 1 (base case)
    # how many times we have encountered 0 as 1 so far here


    odd_count ={0: 1}

    # Initialize variables for the answer and the temporary count of odds
    answer = temp_odd_count = 0

    # Iterate over each value in the list
    for value in nums:
        print(value)
        # Increment temp_odd_count if value is odd

        if value %2 != 0:
            print('come here')
            temp_odd_count +=1


        # If there are at least k odd numbers, add the count to answer
        # This checks if a valid subarray ending at the current index exists
        answer += odd_count.get(temp_odd_count - k, 0)
        
        if temp_odd_count not in odd_count:
            odd_count[temp_odd_count] = 0
            # Increment the count of the current number of odd integers seen so far
            odd_count[temp_odd_count] += 1
        print(odd_count)
    # Return the total number of valid subarrays
    return answer


print(numberOfSubarrays([1,1,2,1,1], 3))