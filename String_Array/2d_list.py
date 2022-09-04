nestedList = []
for i in range(3):
    nestedList.append([])

print(nestedList)

# Method 2: Use list comprehension
x = 2
y = 3
# nestedList2 = [[[] for j in range(y)] for i in range(x)]
nestedList2 = [[] for j in range(y)]

print(nestedList2)
