

from collections import defaultdict



# tc - o(s.length + t.length())
def customSortString(s, t):

    # map[char]
    map = defaultdict(int)
    for char in t:
        map[char]+=1

    ans = ""

    # Add all the ones in s first here
    for char in s:
        count = map[char]
        for i in range(count):
            ans+=char

            # Make sure to clear out all the ones that is already in s
            # so they don't occur in t here
            map[char] = 0

    # write all remaining characters that don't occur in s:
    for (c, n) in map.items():
        ans+=(c* map[c])
    print(ans)
customSortString("cba", "abcd")

