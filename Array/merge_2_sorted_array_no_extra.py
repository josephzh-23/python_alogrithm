'''

Have 2 pointers here left and right,

We will declare two pointers i.e. left and right.

The left pointer will point to the last index of the arr1[](i.e. Basically the maximum element of the array).
The right pointer will point to the first index of the arr2[](i.e. Basically the minimum element of the array).

Left pt move towards index 0 and
right pter moves towards index m-1


'''

def merge(arr1, arr2, n, m):
    # Declare 2 pointers:
    left = n - 1
    right = 0

    # Swap the elements until arr1[left] is smaller than arr2[right]:
    while left >= 0 and right < m:
        if arr1[left] > arr2[right]:
            # if arr1[left] > arr2[right], we will swap the elements here

            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break

    # Sort arr1[] and arr2[] individually:
    arr1.sort()
    arr2.sort()

    arr1.extend(arr2)
    print(arr1)


if __name__ == '__main__':
    arr1 = [1, 4, 8, 10]
    arr2 = [2, 3, 9]
    n = 4
    m = 3
    merge(arr1, arr2, n, m)

    print("The merged arrays are:")
    print("arr1[] = ", end="")
    for i in range(n):
        print(arr1[i], end=" ")
    print("\narr2[] = ", end="")
    for i in range(m):
        print(arr2[i], end=" ")
    print()
