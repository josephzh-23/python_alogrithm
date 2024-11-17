from random import random


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        


        '''
This problem can be done with quick select here 

1. And #1 thing to watch out for is 

1. 
Quickselect uses the same idea as Quicksort. First, we choose a pivot index. The most common way to choose the pivot is randomly. 

We partition nums into 3 sections: elements equal to the pivot, elements greater than the pivot, and elements less than the pivot.

Next, we count the elements in each section. Let's denote the sections as follows:

And the below are the 3 sections here 
left is the section with elements less than the pivot
mid is the section with elements equal to the pivot

right is the section with elements greater than the pivot
Quickselect is normally used to find the k 


th
  smallest element, but we want the k 
th
  largest. To account for this, we will swap what left and right represent - left will be the section with elements greater than the pivot, and right will be the section with elements less than the pivot.

Case 1 : 
If the number of elements in left is >= k , the answer must be in left - any other element would be less than the k 
th largest element. We restart the process in left.


Case 2:

If the number of elements in left and mid is less than k, the answer must be in right - any element in left or mid would not be large enough to be the k 
th
  largest element. We restart the process in right.

Any eleemnts on the right would have solved this problem no problem here 


        '''

def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            
            if k <= len(left):
                return quick_select(left, k)
            
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            
            return pivot
        
    