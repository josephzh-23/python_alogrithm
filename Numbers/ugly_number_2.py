#the one below is the solutino here

def uglyNumber(n):

    uglyNumberList = [1]

    twoPosition = 0
    threePosition = 0
    fivePosition = 0
    # because we know that the last element of this list will be the answer we
    # are looking for here
    while len(uglyNumberList) < n:

        '''
        This is the same as the horizontal rows that we have seen refer to the notes as said 
        Until length equal to what we want above there 
        '''
        by2 = uglyNumberList[twoPosition] * 2
        by3 = uglyNumberList[threePosition] * 3
        by5 = uglyNumberList[fivePosition] * 5

        minimum = min(by2, by3, by5) #these 3 are right over here
        uglyNumberList.append(minimum)

        if minimum == by2:
            twoPosition+=1
        if minimum == by3:
            threePosition +=1
        if minimum == by5:
            fivePosition+=1
    return uglyNumberList[-1]













