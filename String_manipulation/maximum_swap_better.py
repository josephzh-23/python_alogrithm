'''
To achieve this effectively,

Step 1
we can traverse the number's digit from right to left
record the index of the largest digit seen so far at each step and its position here

Looking for the 1st digit s[i],


Step 2 here
From left to right then we have

Now that we know, for each position, the largest digit that appears after it, we check if we can make a swap.
The first time we find a digit that is smaller than the largest one that comes after it, we swap them

'''


def maximumSwap(num: int) -> int:
    # Convert the number to a list of its digits in string form.
    digits = list(str(num))
    # Get the length of the list of digits.
    length = len(digits)


    # Create a list to keep track of the indices of the digits
    # that should be considered for swapping.
    max_digit_indices = list(range(length))

    # Populate the max_digit_indices list with the index of the maximum digit
    # from the current position to the end of the list.
    for i in range(length - 2, -1, -1):
        # If the current digit is less than or equal to the maximum digit found
        # to its right, update the max_digit_indices for the current position.
        if digits[i] <= digits[max_digit_indices[i + 1]]:
            max_digit_indices[i] = max_digit_indices[i + 1]

    '''
    
    For 2736 the indices are [1, 1, 3, 3]
    
    For 2, the max indice to right is 7
    For 7, it's 7 
    for 3, it's index = 3 since 3 < 6
    For 6 it's 6 itself
    '''

    print('max digit indices are ', max_digit_indices)
    # Loop through each digit to find the first instance where a swap would
    # increase the value of the number. Swap and break the loop.
    for i in range(length):
        max_index = max_digit_indices[i]
        # If the current digit is smaller than the maximum digit to its right,
        # swap the two digits.
        if digits[i] < digits[max_index]:
            # Swap the current digit with the maximum digit found.
            digits[i], digits[max_index] = digits[max_index], digits[i]
            # Only one swap is needed, so break after swapping.
            break

    # Convert the list of digits back to a string and then to an integer.
    return int(''.join(digits))

# The preceding code defines a member function `maximumSwap` within the class `Solution`,
# which takes an integer `num` and returns the maximum value integer obtained by swapping
# two digits once.
nums = 2736
maximumSwap(nums)
