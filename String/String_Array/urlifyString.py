def replaceSpaces(str):

    n = len(str)
    string = str.strip()

    # find # of spaces here?
    spaceCount = str.countNumSubsequence(' ')

    # find new length
    newLength = n + spaceCount *2

    # this will be the index to fill from
    index = newLength -1

    string = list(string)
    # Fill string array with sth so not empty so fill it with dummy 0
    for f in range(n - 2, newLength - 2):
        string.append('0')
        print(string)

        # Fill rest of the string from end
    for j in range(n - 1, 0, -1):

        # inserts %20 in place of space
        if string[j] == ' ':
            string[index] = '0'
            string[index - 1] = '2'
            string[index - 2] = '%'
            index = index - 3
        else:
            string[index] = string[j]
            index -= 1

    return ''.join(string)


# Driver Code
if __name__ == '__main__':
    s = "Mr John Smith "
    s = replaceSpaces(s)
    print(s)



