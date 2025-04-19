'''


Use prefix sum calculate the sum of subarray here,


'''
from itertools import accumulate
from typing import List


def decrypt(code: List[int], k: int) -> List[int]:
    # Get the length of the code list
    length_of_code = len(code)
    # Initial answer list filled with zeros
    decrypted_code = [0] * length_of_code

    # If k is 0, the task is to return a list of the same length filled with zeros
    if k == 0:
        return decrypted_code

    '''
    Staritng with 
    [5, 7, 1, 4]
    Then we want to transform the above into 
    [5, 7, 1, 4, 5, 7, 1, 4]
    
    [0, 5, 12, 13, 17, 22, 29, 30, 34]
    
    '''
    prefix_sum = list(accumulate(code + code, initial=0))

    ''
    print("the sum is" , prefix_sum)
    # Iterate through each element in the code list to compute its decrypted value
    for i in range(length_of_code):

        '''
        i = 0 (element 5) 
        the sum of the next k = 3 elements is s[0 + 3 + 1] - s[0 + 1], 
        which is s[4] - s[1] = 17 - 5 = 12. 
        
        So, ans[0] becomes 12.
        s[4] - s[1] = 12
        
        For i = 1 (corresponding to element 7),
         the sum is s[1 + 3 + 1] - s[1 + 1],
          which is s[5] - s[2] = 22 - 12 = 10. So, ans[1] becomes 10.
        '''
        if k > 0:
            # If k is positive, sum the next k values from the element's position
            decrypted_code[i] = prefix_sum[i + k + 1] - prefix_sum[i + 1]
        else:
            # If k is negative, sum the k values preceding the element's position
            decrypted_code[i] = prefix_sum[i + length_of_code] - prefix_sum[i + k + length_of_code]

    # Return the decrypted code

    return decrypted_code
decrypt([5, 7, 1, 4] , 3)