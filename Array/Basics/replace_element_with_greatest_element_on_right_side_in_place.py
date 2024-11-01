'''

'''

def ans(arr):
    n = len(arr)

    maxi = -1; temp= 0
    for i in range(n, 0, -1):
        temp = arr[i]
        arr[i] = maxi

        # compare the back value with the temporary one
        maxi = max(temp, maxi)


    return arr