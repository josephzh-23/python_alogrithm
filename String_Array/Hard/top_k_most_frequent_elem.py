from String_Array.findMode import List


# using this approach took O (n)
# using heap would take O (nlogn)

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    # loop thru each item and count how many times
    # it occurs
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    # At index count, append a list to it
    for n, c in count.items():
        freq[c].append(n)

    # Return the results here
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

    # O(n)