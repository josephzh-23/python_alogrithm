
strs = "cool"
res = {}
for s in strs:
    count = [0] * 26  # a.... z
    for c in s:
        # map a to index 0,  map 'z' to index 26
        # and below is the way to achieve that
        count[ord(c) - ord('a')] += 1

        # this needs to be a tuple because list can't take key
    res[tuple(count)] = s