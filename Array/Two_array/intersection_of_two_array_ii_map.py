def intersect(nums1, nums2):
    if (len(nums1) > len(nums2)):
        return intersect(nums2, nums1)
    res = []
    map = {}
    for n in nums1:
        map[n] = map.get(n, 0) + 1

    for n in nums2:
        count = map.get(n, 0)
        if (count > 0):
           res.append(n)
           map[n] = count -1

    return res



# and here is the solutino here
print(intersect([1, 2, 2, 1], [2, 2] ))
print(intersect([4, 9, 5], [9, 4, 9, 8, 4] ))
