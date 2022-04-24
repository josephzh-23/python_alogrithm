
# HERE we will have a list of sample functions and examples that we can reuse
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

thisdict['model'] = "joseph"
print(thisdict)

for item in thisdict.items():
    print(item)
for key in thisdict.keys():
    print(key)

#Iterate thru dictionary
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
d_items = a_dict.items()
