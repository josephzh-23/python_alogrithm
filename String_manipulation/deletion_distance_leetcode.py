'''
the deletion distance of the two strings is the min # of characters you need to deltee in the 2 strings in order to get the
same string. For instance, the deletion distance between "heat" and "hit" is 3

By deleting 'e' and 'a' in "heat,
And by deleting 'i' in 'hit we get the strings "ht" in both cases here

THis is taken from the video of eric programming as said above and before
'''



def deletionDistance(str1, str2):

    arr1 = str1 ; arr2 = str2
    cache = [[0] * len(str1) for j in range(len(str2))]

    print('cache is', cache)
    def dfs(start1, start2):

        if start1 == len(arr1) and start2 == len(arr2): return 0

        # string 2 has more then 0


        # the following are the differences here
        # str2 = "12" str1 = ""
        if start1 == len(arr1): return len(arr1) - start2

        # str1 = "12"  str2= ""
        if start2 == len(arr2): return len(arr2) - start1

        print('start 1 and start 2 is', start1, start2)
        if cache[start1][start2]: return cache[start1][start2]


        # if matche then we can continue here
        if arr1[start1] == arr2[start2]:
            cache[start1][start2] = dfs(start1 + 1, start2 + 1)

        else:
            path1 = dfs(start1 + 1, start2)
            path2 = dfs(start1, start2 + 1)

            cache[start1][start2] = min(path1, path2)

        return cache[start1][start2]

    return dfs(0, 0)


'''
Imagine here the start1 and start2 index are the ones that really matter here 

- 

'''

str1 = "dog"
str2 = "frog"

# and then deleting the items here we would have the thing from before
print(deletionDistance(str1, str2))

