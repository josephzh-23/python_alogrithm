thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"}) # change the existing item here

for x in thisdict.keys():
  print(x)