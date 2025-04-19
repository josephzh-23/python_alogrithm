''' Wee

we can solve this using the indegree approach here as said
'''
from collections import defaultdict, Counter, deque
from typing import List



def alienOrder(words: List[str]) -> str:
    # Step 0: create data structures + the in_degree of each unique letter to 0.
    adj_list = defaultdict(set)

    # Counter({'w': 0, 'r': 0, 't': 0, 'f': 0, 'e': 0})
    in_degree = Counter({c: 0 for word in words for c in word})


    # Step 1: We need to populate adj_list and in_degree.
    # For each pair of adjacent words...

    '''
    The way you are comparing here are 
    You are comparing word by word 
    1st with 2nd, and 2nd with 3rd and so forth, character by character here 
    
    So you have 
    'w'     'w'
    
    
    '''
    for first_word, second_word in zip(words, words[1:]):
        for c, d in zip(first_word, second_word):

            print('c and d are', c, d)
            if c != d:

                '''
                Basically anything with a d 
                '''
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    in_degree[d] += 1
                break
        else:  # Check that second word isn't a prefix of first word.
            if len(second_word) < len(first_word):
                return ""

    # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
    output = []
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    while queue:
        c = queue.popleft()
        output.append(c)
        for d in adj_list[c]:
            in_degree[d] -= 1

            '''
            This way we can add item with the indegree == 0 last using this approach here 
            '''
            if in_degree[d] == 0:
                queue.append(d)

    # If not all letters are in output, that means there was a cycle and so
    # no valid ordering. Return "" as per the problem description.
    if len(output) < len(in_degree):
        return ""
    # Otherwise, convert the ordering we found into a string and return it.
    return "".join(output)

alienOrder(["wrt","wrf","er","ett","rftt"])
