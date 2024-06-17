from typing import List

from Heap.max_heap import MaxHeap

'''
This is the 2nd versino of that problem that needs to be done right now 

Step 1: 
What's a cycle here?

In each iteration, a cycle of length n + 1 is considered, signifying the time needed to execute tasks without 
violating the cooling period constraint.
 
 For instance, if there are 2 tasks (A) and n = 2, the iterations required 
would be A-Idle-Idle-A (n + 1 iterations before picking a new task A). That would be it here 

Step 2: 
Complete the cycle here and then rebuild the heap with udpated frequencies here 

'''

def leastInterval(tasks: List[str], n: int) -> int:
    # Build frequency map
    freq = [0] * 26
    for ch in tasks:
        freq[ord(ch) - ord('A')] += 1

    # Max heap to store frequencies
    # pq = [-f for f in freq if f > 0]
    # heapq.heapify(pq)
    pq = MaxHeap()
    for f in freq:
        pq.push(f)
    time = 0
    # Process tasks until the heap is empty
    while pq:
        cycle = n + 1
        store = []


        task_count = 0
        # Execute tasks in each cycle
        while cycle > 0 and pq:
            current_freq = pq.pop()
            if current_freq > 1:
                store.append(current_freq - 1)
            task_count += 1
            cycle -= 1

            # you mean this is here how it is for me
        # Restore updated frequencies to the heap
        for x in store:
            pq.push(x)
        # Add time for the completed cycle
        time += task_count if not pq else n + 1
    return time

leastInterval()