'''

The second solutino for solving this question here

Want to think of a better appraoch here

We can try thsi wirh brute force here and see how goes here?

Here if we try both of these things it will be good here

O(n^2) this is an improvement over the follwoing solution

function solution(array)
    for i in (0 to len(array))
        for j in (i to len(array))
            res += min(A[i:j])

            this is an O(n) operation here, comparing everythign so far here
    return res
'''

def bruteForce(arr):
    sum = 0
    for i in range(len(arr)):

        mini=  arr[i]
        for j in range(i, len(arr)):
            mini = min(mini, arr[j])
            '''
            [3]
            [3, 1] 
            [3, 1, 2]   // 2
            
            '''
            sum = sum + mini

    return sum
    print(sum)

bruteForce([3, 1, 2, 4])