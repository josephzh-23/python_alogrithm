

'''
s = "ABC"
“ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”

Input: S = “XY”
Output: “XY”, “YX”

'''
# permutation of string here and then keep going here

# here we pass the list in if possible
def permutate(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permutate(a, l + 1, r)
            a[l], a[i] = a[i], a[l]
def toString(List):
    return ''.join(List)