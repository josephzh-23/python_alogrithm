

def generateParenthesis(n):

    list = []
    backtrack(list, "", 0, 0, n)

    return list

def backtrack(arr, curString, openCount, closeCount, max)


    if(len(curString) == max*2):
        arr.add(curString)

    if(openCount< max):
        backtrack(arr, curString+ "(", openCount +1, close, max)
    if (closeCount< open):
        backtrack(arr, curString + ")", openCount, closeCount+1, max)