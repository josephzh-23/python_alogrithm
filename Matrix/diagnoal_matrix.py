
'''
We can change the direction each time we reached the top and then we
would come back down


'''
# matrix here would be 2d as said before
def findDiagnoalOrder(mat):

    # and then here we would have the code

    res = []
    rows = len(mat)
    cols = len(mat[0])

    res = []
    currow = curcol = 0

    goingUp = True

    while len(res) != rows * cols:
        if goingUp:
            while currow >= 0 and curcol <= cols:

                res.append(mat[currow][curcol])

                currow -=1
                curcol +=1

            # if reached to the last column here
            if curcol == cols:
                curcol-=1
                currow +=2
            else:
                currow +=1

            goingUp = False

        else:

            # we reached the last row and now the curcol is < 0
            while currow < rows and curcol >=0:
                res.append(mat[currow][curcol])

                curcol -=1
                currow +=1

            if currow == rows:
                curcol+=2
                currow -=1
            else:
                curcol+=1
            goingUp = True

    return True

'''
T: O(n)
S: O(n) as a space O(n) here 
'''

