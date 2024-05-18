# Python program to illustrate
# enumerate function
from collections import Counter

l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
num = [1, 2, 3, 4, 5]
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
obj3 = enumerate(num)

c = Counter(num)
# print(c)

for n in c:
    print( n)
# print("Return type:", type(obj1))
# print(list(obj3))
# print(list(enumerate(l1)))


# changing start index to 2 from 0
print(list(enumerate(s1, 2)))