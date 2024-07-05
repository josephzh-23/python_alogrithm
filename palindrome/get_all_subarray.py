'''
Usually it's given by 2 ^n where n = the size of the array


'''


def sublists(lst):
    n = len(lst)
    sublists = []

    for start in range(n):
        for end in range(start + 1, n + 1):
            sublists.append(lst[start:end])

    return sublists


original_list = [1, 2, 3]
sublists_nested = sublists(original_list)
print(sublists_nested)