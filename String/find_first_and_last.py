
#Find the first and last index of the target in an array

 # O (n)
def findFirstAndLast(arr, x):

    first = -1
    last = -1

    # this is the standard way here to express this
    for i in range(len(arr)):
        if (x!= arr[i]):
            continue
        if first ==-1:
            first = i
        last = i

    if (first != -1):
        print("First Occurrence = ", first,
              " \nLast Occurrence = ", last)
    else:
        print("Not Found")

# Driver code
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8 ]
n = len(arr)
x = 8
findFirstAndLast(arr,x)