
# Python 3 program to print all
# possible strings of length k




# The method that prints all
# possible strings of length k.
# It is mainly a wrapper over
# recursive function printAllKLengthRec()
def printAllKLength(set, k):

    n = len(set)
    printAllKLengthRec(set, "", n, k)


def printAllKLengthRec(set, prefix, n, k):

    # Base case: k is 0,
    # print prefix
    if (k == 0) :
        print(prefix)
        return

    for i in range(n):
        newPrefix = prefix + set[i]
        if i == k:
            print(newPrefix)
        printAllKLengthRec(set, newPrefix, n, k - 1)

# Driver Code
if __name__ == "__main__":

    print("First Test")
    set1 = ['a', 'b']
    k = 3
    printAllKLength(set1, k)


