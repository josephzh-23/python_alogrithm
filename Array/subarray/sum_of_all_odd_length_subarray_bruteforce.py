'''
class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int n = arr.length;
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if ((j - i + 1) % 2 == 0) continue;
                for (int k = i; k <= j; k++) {
                    res += arr[k];
                }
            }
        }
        return res;
    }
}

'''
from typing import List

'''

O(n^3)
'''

def sumOddLengthSubarrays( arr: List[int]) -> int:
    n = len(arr)
    answer = 0

    numOfOddLengthArray= 0
    # get the number of subarrays first here

    for left in range(n):
        for right in range(left, n):
            if (right - left + 1) % 2 == 1:
                current_sum = 0
                for index in range(left, right + 1):
                    current_sum += arr[index]
                answer += current_sum
    print(numOfOddLengthArray)
    return answer
arr = [1,4,2,5,3]
sumOddLengthSubarrays(arr)