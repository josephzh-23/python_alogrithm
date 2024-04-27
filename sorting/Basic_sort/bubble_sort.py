
# best case O(n)
# worst case O(n^2)


'''
A little more in depth here of how this works,
Bubble sort here

1. . For that, we will select a certain range of an unsorted array in the code

2. Within this loop then, runs from 0 to i-1 though the range is from 0 to i) to push the maximum element
to the lastindex of the selected range, by repeatedly swapping adjacent elements.

    - like in the following wayswap the adjacent element by repeatedly swapping adjacent element here,

3.Thus, after each iteration, the last part of the array will become sorted.

4. After (n-1) iteration, the whole array will be sorted.

5. Here, after each iteration, the array becomes sorted up to the last index of the range. That is why the last index
of the range decreases by 1 after each iteration.
This decrement is achieved by the outer loop and the last index is
represented by variable i in the following code. And the inner loop(i.e. j) helps to push the maximum element of

range [0….i] to the last index(i.e. index i). '''



# THis is the most basic sort, you just compare and swap
def bubbleSort (arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will, this is the inner loop that we talked about previously here
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

for i in range (len(arr)):
    print("%d " %arr[i])