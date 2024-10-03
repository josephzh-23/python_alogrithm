'''


[0, 1,0, 3, 12]

253 here
'''


'''
The above would swap automatically you don't have to change anything
'''
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def moveZeros(arr):
    i, j = 0, 0

    while i < len(arr) and j < len(arr):

        while arr[j] == 0:
            j+=1

        if arr[i] == 0 and arr[j] != 0:
            swap(arr, i, j)
        i+=1
        j+=1
    print(arr)
nums = [0, 1, 0, 3, 12]
moveZeros(nums)