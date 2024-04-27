

'''
Quick sort step 1:

1. Choose a value in the array to be the pivot element.
2. Order the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.

3. Swap the pivot element with the first element of the higher values so that the
 pivot element lands in between the lower and higher values.
Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.

And then here we continue to have the following here:
What's quick sort algo?

[ 11, 9, 12, 7, 3]

Choose value 3 as pivot element, break down and dont' read too fast

The rest of the values in the array are all lower than 3,
 an must be on the right side of 3. Swap 3 with 11.

[ 3, 9, 12, 7, 11]

Step 3:
Value 3 is now in the correct position.
We need to sort the values to the right of 3. We choose the last value 11 as the new pivot element.
[3, 9 12, 7, 11]

Step 4:
[3, 9, 12, 7, 11]     # here then

step 5:
 The value 7 must be to the left of pivot value 11, and 12 must be to the right of it. Move 7 and 12.
 [ 3, 9, 7, 11, 12]

'''

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)