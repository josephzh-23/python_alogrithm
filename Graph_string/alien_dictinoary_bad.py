'''


Words are sorted lexiographically here


Topoligcal sort problem here

1.  If words are sorted lexicographically, the first different character from word[i] and word[i+1] sets an ordering rule.

2. an improper ordering like a word being a prefix of a previous word but appearing later in the list.

3. Assuming the ordering rules do not contain contradictions,
perform a topological sort on the graph to find the alien language character order.

4.  ['z', x , z]

We do the s[ord('z') - ord('a')] = true     set this to true


'''
from collections import deque
from typing import List
arr =[1, 2, 3, 4]

def alienOrder(self, words: List[str]) -> str:
    # Graph representation - 26 characters for 26 lowercase letters
    graph = [[False] * 26 for _ in range(26)]

    # Seen array to keep track of which characters are present in the words list
    seen = [False] * 26

    # Counter for the number of unique characters
    unique_char_count = 0

    # Length of the words list
    words_count = len(words)

    # Process all the words for character presence and ordering

    #
    for i in range(words_count - 1):
        # Record the characters in current word as seen
        for char in words[i]:
            if unique_char_count == 26:
                break


            index = ord(char) - ord('a')
            if not seen[index]:
                unique_char_count += 1
                seen[index] = True
        word_length = len(words[i])

        # Compare characters and establish ordering
        for j in range(word_length):

            # If the next word is shorter than the current word, there is an issue with the order
            if j >= len(words[i + 1]):
                return ''

            '''
            
            Compare the 2 characters of word[i] and word[i + 1]
            'abc'   'abc' 
            graph[0][1] = true
            
            that means the above there is a relationship above and that's step # 1 here 
            '''
            char1, char2 = words[i][j], words[i + 1][j]
            if char1 == char2:
                continue
            index1, index2 = ord(char1) - ord('a'), ord(char2) - ord('a')


            if graph[index2][index1]:  # If there is a cycle, return empty string
                return ''
            graph[index1][index2] = True
            break
    '''
        Check the last word for new characters
    
    '''
    for char in words[words_count - 1]:
        if unique_char_count == 26:
            break
        index = ord(char) - ord('a')
        if not seen[index]:
            unique_char_count += 1
            seen[index] = True
    '''
    
    '''
    # Calculate in-degree for each character that is seen
    in_degree = [0] * 26
    for i in range(26):
        for j in range(26):
            '''
            both characters are seen 
        
        basically the jth index would have a parent here 
        if graph[i]][j] 
            '''
            if i != j and seen[i] and seen[j] and graph[i][j]:
                in_degree[j] += 1

    # Initialize the queue for topological sort
    queue = deque()
    # Hold characters of the alien language in order
    ordered_chars = []

    # Find characters with in-degree of 0 to start topological sort
    '''
    
    
    '''
    for i in range(26):
        if seen[i] and in_degree[i] == 0:
            queue.append(i)

    # Run topological sort
    while queue:
        current_char_index = queue.popleft()
        ordered_chars.append(chr(current_char_index + ord('a')))

        # Decrease the in-degree of adjacent characters and add new 0 in-degree characters to the queue
        for i in range(26):
            if seen[i] and i != current_char_index and graph[current_char_index][i]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

    # If the length of the ordered characters is less than total unique characters, ordering is not possible
    return '' if len(ordered_chars) < unique_char_count else ''.join(ordered_chars)
