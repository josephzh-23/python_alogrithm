'''
Question: sum of all odd length subarrays


https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/
Using a for and a while loop together here

'''

arr = [ 1, 4, 2, 5, 3]

def sumOddLengthSubarrays(arr):
    totalSum= 0
    # skip by 2 here
    for size in range(1, len(arr) + 1, 2):

        l, r, sum = 0, 0, 0

        while l + size - 1 <= len(arr) and r < len(arr):

            sum+= arr[r]
            r+=1

            # let's use the max os light here



# and then using the code here we have way much better data
            '''
            size = 1 
            
            '''
            if r -l >= size:
                totalSum += sum
                sum -= arr[l]
                l+=1

    print(totalSum)
    return totalSum


sumOddLengthSubarrays(arr)