dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "count": 0
}

# To add sth to dictionary
key = "joseph"
dict[key] ="I am cool here"
print("the key value is", dict[key])


dict.update({"color": "red"}) # change the existing item here

val = dict.get("count") +1
print("the value is ", val)


'''
The following returns 0 if "chill" is not found 
in the following 
 '''
nonExist = dict.get("chill",0)
print("the non-existing value is ", nonExist)




