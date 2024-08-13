from typing import List

'''

1. Use a dict and a value
2. At the end  for item in dict.values():
        print(item)
        result.append(item)
Use dict{}, pretty simple 
   for word in strs:
        sortedword = "".join(sorted(word))
        
    - dict[sortedword] = word
    - dict[sortedword].append(word)



'''
def groupAnagrams(strs:List[str]) -> List[List[str]]:

    dict = {}
    for word in strs:
        sortedword = "".join(sorted(word))

        # at the start, make a list and then add to it
        if sortedword not in dict:
            # print(sortedword)
            dict[sortedword] =[word]
        else:
            dict[sortedword].append(word)

    result = []
    for item in dict.values():
        print(item)
        result.append(item)
    return result

list = ['cat', 'dog', 'tac', 'god', 'act']
groupAnagrams(list)