
'''

YOu have a list of amazon web requests here and then you have
where each request entry contains (time, customerId, page visited).

Find the most visited n-consecutive page sequence. Where n can vary
(time, customerId, page)
[
    (1, 'A', 'home'),
    (2, 'A', 'about'),
    (3, 'A', 'products'),
    (4, 'A', 'contact'),

    (5, 'B', 'home'),
    (6, 'B', 'products'),
    (7, 'B', 'contact'),

    (8, 'C', 'home'),
    (9, 'C', 'about'),
    (10, 'C', 'products'),
    (11, 'C', 'contact'),
]


	1.	Group logs by customerId and sort them by time.
	2.	For each customer, extract all n-length consecutive sequences.
	3.	Count each sequence globally.
	4.	Return the sequence with the highest frequency.

'''
from collections import Counter, defaultdict
from typing import DefaultDict

'''
The sequence we are looking for is 3 here 
'''

logs = [
    (1, 'A', 'home'),
    (2, 'A', 'about'),
    (3, 'A', 'products'),
    (4, 'A', 'contact'),

    (5, 'B', 'home'),
    (6, 'B', 'products'),
    (7, 'B', 'contact'),

    (8, 'C', 'home'),
    (9, 'C', 'about'),
    (10, 'C', 'products'),
    (11, 'C', 'contact'),
]
def answer(logs, n):
    '''

    Sort by the time first
    '''
    logs.sort(key=lambda x: x[0])
    userVisit = defaultdict(list)
    '''
    Basied on above, we then have the code 
    1: [home, products, contact]
    '''
    for time, userId,page in logs:
        userVisit[userId].append(page)

    '''
      # Step 2: Extract n-length sequences per user
      Here we are using a list as a key 
      
    
    '''
    seqCounter = Counter()

    for visits in userVisit.values():
        if len(visits) < n:
            continue
        '''
        This is a smart sliding window
        
        '''
        for i in range(len(visits) - n + 1):
            seq = tuple(visits[i:i + n])

            s = set()
            if seq not in s:
                seqCounter[seq] +=1
            s.add(seq)
    print(seqCounter)
answer(logs, 3)

