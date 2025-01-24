from Binary_Search.Basic.find_first_match_binary_search import lower_bound
from Binary_Search.Basic.find_first_value_smaller_or_equal import find_first_smaller_or_equal
from Binary_Search.Basic.find_last_value_smaller_or_equal_to import find_last_smaller_equal


def mostJobAssigningWorkBinarySearch(difficulty, profit, worker):
    job_count = len(difficulty)
    # Pairing each job's difficulty with its profit and storing them as tuples
    jobs = [(difficulty[i], profit[i]) for i in range(job_count)]
    profit.sort()
    # Sorting jobs based on their difficulty, important
    jobs.sort(key=lambda x: x[0])
    # Sorting workers based on their capabilities
    worker.sort()
    totalProfit = 0
    for capacity in worker:
        print(capacity)
        firstDifficultyMatchingWorker = find_last_smaller_equal(difficulty, capacity)
        print(firstDifficultyMatchingWorker, worker, difficulty)
        job_index = firstDifficultyMatchingWorker
        totalProfit+= profit[job_index]
    print(totalProfit)
difficulty = [2, 4, 6, 8]
profit = [20, 40, 70, 80]
worker = [2, 7, 5]
mostJobAssigningWorkBinarySearch(difficulty, profit, worker)