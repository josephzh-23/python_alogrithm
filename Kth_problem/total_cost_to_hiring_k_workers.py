'''
What's k = 3 : 1 worker each sessoin so 3 sessions,
Candidates: hire either the first canddiate workers or the last canddiate workers here
need to go from all directions here

Candidates here:
'''
from Queue_heap.max_heap import MinHeap


def totalCostHiringKWorkers(costs, k, candidates):
    #
    q = MinHeap()

    # the first few ppl here
    firstCosts = sum(costs[:candidates])
    lastCosts = sum(costs[-candidates:])

    # for each candidate we take off ppl,
    # [17, 12, 10,7, 11, 20, 8], need to remove here first
    # for candidate in candidates:
    # check if there is a tie first, if then add everything
    if firstCosts == lastCosts:
        for i, c in enumerate(costs):
            q.push((c, i))
    # in the first and the last one here
    #
    # print(q.pop())
    # print(q.pop())
    # print(q.pop())
    totalCosts = 0
    for c in range(k):
        # print(q.pop())
        totalCosts += q.pop()[0]


    print(totalCosts)




# costs = [17,12,10,2,7,2,11,20,8]; k = 3; candidates = 4

costs = [1, 2, 4, 1]; k = 3; candidates = 3
totalCostHiringKWorkers(costs, k,candidates)