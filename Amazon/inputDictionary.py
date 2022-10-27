# 2


# 2 d better python solution

n =5
adj = {u: [] for u in range(n)}

adj[0].append(1)



# print(adj)
print(adj[0][0])

#sam 6047830249

input = [
        'sam 99912222',
        'tom 11122222',
        'harry 12299933',
        'jerry',
        'edward',
        'ff']

d = dict()
for item in input:
    value = item.split(" ")
    print(value)
    print('length of value is ', len(value))
    if len(value) >1:
        d[value[0]] = value[1]
    else:
        d[value[0]] = []
    # dict[value[0]] = value[1]
    # print(value)

print(d)