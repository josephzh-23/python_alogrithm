'''

n workers
difficulties
profit
worker

difficulty = [2,4,6,8,10],
 profit = [10,20,30,40,50],
 worker = [4,5,6,7]

 After assigning the worker to the jobs the maximum that can complete


and m workers

'''
from typing import List


'''

Match worker with the best job here 
- 

The intuition behind the solution is to first sort the jobs based on their difficulty, ensuring that we always encounter the less difficult jobs first. Simultaneously, we sort the workers based on their ability so we can sequentially assign them to jobs without backtracking. After this, we can iterate through the workers in ascending order of their ability.

2. For each worker, we iterate through the sorted jobs, updating the maximum profit (t) that this worker can generate (only if the job difficulty is less than or equal to the worker's ability). Since the jobs are sorted by difficulty, once a job's difficulty is greater than a worker's ability, we can stop the search for that worker and proceed to the next one, because all subsequent jobs will also be too difficult.

THis is where the binary search happens here 

3. 
'''
from typing import List





class Solution:
    def max_profit_assignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job_count = len(difficulty)
        # Pairing each job's difficulty with its profit and storing them as tuples
        jobs = [(difficulty[i], profit[i]) for i in range(job_count)]


        # Sorting jobs based on their difficulty, important
        jobs.sort(key=lambda x: x[0])
        # Sorting workers based on their capabilities
        worker.sort()

        max_profit = 0  # Tracks the maximum profit that can be achieved so far
        total_profit = 0  # Summing up the total profit for all workers

        job_index = 0  # Index to keep track of the current job

        # the job index never goes back to 0 here this is very important
        # Iterating through each worker
        for capability in worker:

            # Updating the max_profit by comparing with each job's profit if the worker can handle the job
            while job_index < job_count and jobs[job_index][0] <= capability:
                max_profit = max(max_profit, jobs[job_index][1])
                job_index += 1
            # Accumulating the profit earned by this worker based on max_profit so far
            total_profit += max_profit

        # Returning the total profit that can be earned by all workers
        return total_profit