# from collections import dict_items
thislist = ["apple", "banana", "cherry"]

# to add to the list using
thislist.append("orange")
thislist.remove("banana")
print(thislist)


# and to print this
for x in thislist:
  print(x)

# Print based on the index
for i in range(len(thislist)):
  print(thislist[i])

#return the 1st to the 2nd element in list
print(thislist[1:2])
