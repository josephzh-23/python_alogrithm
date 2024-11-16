'''


Intuition

Let's imagine the indices of s as a graph. Each index can be thought of as a node, which represents building s up to the index.

Adding a word to an existing string is like an edge between nodes. '
For a node start, we can move to node end if the substring of s between start, end exists in wordDict.



For example, let's say we have s = "leetcode" and wordDict = ["leet", "code"].

We are currently at node 4, which implies that we have built "leet" (the first 4 characters of s).
We can move to node 8, because the substring of s with indices [4, 8) is "code", which is in wordDict.


We start at node 0, which represents the empty string. We want to reach node s.length, which implies that we have
 built the entire string. We can run a BFS to accomplish this traversal.

  If you're not familiar with BFS, check out the relevant Explore Card.

At each node start, we iterate over all the nodes end that come after start.

For each end, we check if the substring between start, end is in wordDict. If it is, we can add end to the queue.

    We will first convert wordDict into a set so that we can perform the checks in constant time. We will also use a data structure seen to prevent us from visiting a node more than once.
'''
from collections import deque


def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    words = set(wordDict)
    queue = deque([0])
    seen = set()

    while queue:
        start = queue.popleft()
        if start == len(s):
            return True

        for end in range(start + 1, len(s) + 1):
            if end in seen:
                continue

            if s[start:end] in words:
                queue.append(end)
                seen.add(end)

    return False