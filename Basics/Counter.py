# import counter class from collections module
# from collections import Counter
#
# # Creation of a Counter Class object using
# # string as an iterable data container
# x = Counter("geeksforgeeks")
# 1
# # printing the elements of counter object
# # you can then print it here
# for i in x.items():
#     print(i, end=" ")
#
# # can also do the following turn into the map
# d = dict(Counter("323"))
from collections import Counter

d = Counter()

d[0]+=1
print(d)