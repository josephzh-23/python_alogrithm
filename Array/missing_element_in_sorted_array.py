''' T

Input: nums = [4,7,9,10], k = 1
Output: 5
Explanation: The first missing number is 5.

Missing elemetn in sorted array here

Another approach to solving this problem is to use binary search. Instead of focusing on the number of missing elements in every two adjacent numbers like nums[i] and nums[i + 1].
We will focus on the total number of missing elements on nums[i]'s left, that is, within the range [nums[0], nums[i]].

    And then the next part here is

1) For an index i:
  [4,7, 9, 10 ]

How to find the # of missing elements here:
    The number of positive integers missing before each index is equal to nums[idx] -
idx - nums[0]. This is because,
 if there are no missing elements, nums[idx] = nums[0] + idx + 0 (zero missing elements).

 If there are k missing elements, then nums[idx] = nums[0] + idx + k.
To find k, we move the elements to the left of the equation thus giving us: k = nums[idx] - nums[0] - idx;


Example here:
    - [4, 7, 9, 10]
    # of missing elments from before 9 at idex 2
    = nums[2] - nums[0] - 2 = 3     which is [5, 6, 8]


The actual algorithm here

To find the kth missing element,
 we need to find range of indices in which k missing elements can be found.

Let's say we want the third missing element, k = 3.
Let's apply binary search on the sorted array, start with the full range of the sorted array:
    left = 0, right = nums.length - 1 = 3;

1) Find the mid = left + (right - left) / 2 = 0 + (3 - 0) / 2 = 1;
2) The number of missing elements before index 1 is 2 from the above calculation is 2. We need the 3th missing element, so we need to search further on the right side of the array so that we can get more missing elements.
Update the left = mid + 1 = 2;

    3) Calculate the mid again = left + (right - left) / 2 = 2 + (3 - 2) / 2= 2

The number of missing elements before index 2 is 3 from the above calculation. Since we have k elements, we move to the left half.
Update right = mid - 1 = 1
Now right is smaller than left so we break out of the loop.
-

In summary:
The kth missing element is between nums[right] and nums[right + 1]. That is, between 7 and 9.
The kth missing number can therefore be calculated through the equation below:
    nums[right] + k - number of elements missing before index right.
    nums[right] + k - (nums[right] - nums[0] - right) = k - (nums[0] - right) = k + nums[0] + right


'''


'''
To find # of missing positive integers before index 
'''
def missingElementsBeforeIndex(index, nums):
    return nums[index] - nums[0] - index


def missingElement(nums, k):
    l= 0; r = len(nums) - 1
    while l < r:

        mid = l + (r - l )//2

        ''' 
        if # of positive interger missing before arr[mid]
        < k, search on the right 
        '''
        if missingElementsBeforeIndex(mid, nums) < k:
            l = mid + 1
        else:
            r = mid -1

        # nums[right] + k - (nums[right] - nums[0] - right)
        # = k - (nums[0] - right) = k + nums[0] + right

        return k + nums[0] + r