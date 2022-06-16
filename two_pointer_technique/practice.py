

# find that index here
def binSearch(arr, l, r, tar):

    mid = (r+l)//2

    if l <= r:
        if arr[mid] > tar:
            return binSearch(arr, l, mid-1, tar)
        if arr[mid] < tar:
            return binSearch(arr, mid+1, r, tar)
        else:
            return mid

    else:
        return -1


arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binSearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")