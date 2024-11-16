'''
We will keep a for loop with a running map here to make things simple here

Can be applied to
1) Count number of nice subarrays prefix sum problem here

'''


def numberOfSubarrays(nums: List[int], k: int) -> int:
    # Initialize counter for odd counts with 0 count as 1 (base case)
    # how many times we have encountered 0 as 1 so far here

    odd_count = {0: 1}

    # Initialize variables for the answer and the temporary count of odds
    answer = temp_odd_count = 0

    # Iterate over each value in the list
    for value in nums:
        print(value)
        # Increment temp_odd_count if value is odd

        if value % 2 != 0:
            print('come here')
            temp_odd_count += 1

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
