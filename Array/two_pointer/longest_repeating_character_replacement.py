'''
Longest repeating character replacement here

- "AABEAFACAAEAA" k = 1 here,

Can do a 1 operation here,

    Dynamic sliding window here

    Let's take two pointers start and end. These pointers point to the start and end of the window. count (which is set as 0 initially) to record the number of As in the current window.

     We call a window valid only if the difference between the size of the window and count is less than or equal to k.

     end+1−start−count<=k

That's the one above here

    The variable count increases when the window grows, and the new character entering the window is A. On the opposite side, when the window shrinks and the outgoing character is A, we decrease count.

Use maxLength to track the maximum length here

-
'''


def characterReplacement(self, s: str, k: int) -> int:
    all_letters = set(s)
    max_length = 0

    # iterate over each unique letter
    for letter in all_letters:
        start = 0
        count = 0

        # initialize a sliding window for each unique letter
        for end in range(len(s)):
            if s[end] == letter:
                # if the letter matches, increase the count
                count += 1

            # bring start forward until the window is valid again
            while not self.__is_window_valid(start, end, count, k):
                if s[start] == letter:
                    # if the letter matches, decrease the count
                    count -= 1
                start += 1

            # at this point the window is valid, update max_length
            max_length = max(max_length, end + 1 - start)

    return max_length


def __is_window_valid( start: int, end: int, count: int, k: int):
    return end + 1 - start - count <= k