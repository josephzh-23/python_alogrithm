'''

https://www.youtube.com/watch?v=4zNK0rhFfcA
The solutino is taken from neetcode.io


k odd nubmers on it

Sliding window problem here

# keep a running count of
how many times each count of odd numbers has occurred in our running total (prefix).


Step 1:
Let's say we're iterating through the array and at some point we have encountered x odd numbers. Now,
if
at an earlier point in the array we had encountered x - k odd numbers,

 any subarray starting from that earlier
point to our current position will have exactly k odd numbers. Why? Because x - (x - k) = k.


Step 2:

What this looks like
if numOdd < k:
keep moving r to the right
[ 2, 2, 1, 1, 2, 1, 1 ]
                 r
 l
 m

if numOdd = k
 [ 2, 2, 1, 1, 2, 1, 1 ]
         m        r
 l
 Move up the m pointer
  res = m - l + 1


if numOdd > k:
 [ 2, 2, 1, 1, 2, 1, 1 ]
            m        r
            l
Move l up to 1 there,



'''

def numberOfSubarrays(arr, k):
    # keep track of smallest subarray length
    sum, l, r, minLen = 0, 0, 0, float('inf')

    numOfOdds = 0

    # the total # of subarray here
    total = 0
    while (l < len(arr)):
        '''
        if window's leading edge has NOT reached the end of the array
        AND window's values do NOT add up to num, grow window to right
        '''
        if r < len(arr) and numOfOdds < k:
            if arr[r] % 2 != 0:
                numOfOdds+=1


            r += 1
        elif numOfOdds== k:
            total +=1
            l += 1
        elif numOfOdds > k:
            numOfOdds-=1
            l+=1
        else:
            break
    print("number here is ", total)

    # return 0 if minLen == float('inf') else minLen

# numberOfSubarrays([1,1,2,1,1], k = 3)
numberOfSubarrays([2,2,2,1,2,2,1,2,2,2],  2)