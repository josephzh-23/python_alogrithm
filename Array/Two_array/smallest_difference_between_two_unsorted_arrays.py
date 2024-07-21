'''
A: {1, 2, 11, 15}
B: {4, 12, 19, 23, 127, 235}


'''


def howToDealWithThis(a, b):
    l, r = 0, 0
    diff = 0
    # we use the difference here
    while l < len(a) and r < len(b):
        if a[l] < b[r]:
            inc(l)

        if a[l] > b[r]:
            inc(r)

        diff = min(b[r] - a[r], diff)


def inc(number):
    number+=1
    return number

for i in range(100):
    inc(i)
# print(inc(5))