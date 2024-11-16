'''


Given an m * n integer array

if 3 or more
'''
from typing import List

candy = [[1,3,5,5,2],
         [3,4,3,3,1],
         [3,2,4,5,2],
         [2,4,4,5,5],
         [1,4,4,1,1]]



'''
An example here would we have the code here where 
We begin with 


    1 1 1
    2 2 3
    3 3 2
    
After part 1 marking it becomes then it becomes 

    -1 -1 -1 
    2   2  3
    3   3  2 
    
2. Horizontal and vertical crushign which becomes 
    0  0  0
    2  2  3
    3  3  2
    
3. We need to let the unmarked(postiive) candies fall down then 
to the current position 

 if an empty space on the board has candies on top of itself, then these candies will drop
  until they hit a candy or bottom at the same time. No new candies will drop outside the top boundary.
0 0 0
0 0 0
2 2 3
    
And then becomes 


'''
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # Dimensions of the board
        num_rows, num_cols = len(board), len(board[0])

        # Flag to indicate if we should continue crushing candies
        should_crush = True


        '''
        Mark # 1 part for horizontal crushing here 
        
        '''
        # Keep crushing candies until no more moves can be made
        while should_crush:
            should_crush = False  # Reset the flag for each iteration

            # Mark the candies to be crushed horizontally
            for row in range(num_rows):
                for col in range(num_cols - 2):
                    candy_value = abs(board[row][col])
                    # Check if three consecutive candies have the same value
                    if candy_value != 0 and candy_value == abs(board[row][col + 1]) == abs(board[row][col + 2]):
                        should_crush = True  # We will need another pass after crushing
                        # Mark the candies for crushing by negating their value
                        board[row][col] = board[row][col + 1] = board[row][col + 2] = -candy_value
            '''
            Part 2 marking vertical here 
            
            
            
            '''
            # Mark the candies to be crushed vertically
            for col in range(num_cols):
                for row in range(num_rows - 2):
                    candy_value = abs(board[row][col])
                    # Check if three consecutive candies vertically have the same value
                    if candy_value != 0 and candy_value == abs(board[row + 1][col]) == abs(board[row + 2][col]):
                        should_crush = True  # We will need another pass after crushing
                        # Mark the candies for crushing
                        board[row][col] = board[row + 1][col] = board[row + 2][col] = -candy_value
            '''
            
            Then we drop the candy down to crush the following ones here 
            and then here this is part 1 here 
            
            1. 
            '''
            # Drop the candies to fill the empty spaces caused by crushing
            if should_crush:
                for col in range(num_cols):
                    # Pointer to where the next non-crushed candy will fall
                    write_row = num_rows - 1
                    for row in range(num_rows - 1, -1, -1):


                        # If the candy is not marked for crushing, bring it down
                        if board[row][col] > 0:
                            board[write_row][col] = board[row][col]
                            write_row -= 1
                    # Fill the remaining spaces at the top with zeros
                    while write_row >= 0:
                        board[write_row][col] = 0
                        write_row -= 1