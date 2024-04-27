'''
slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0,15], [60, 70]]
dur = 8

teh amount of time they want to meet for
Output:
1. [60, 68]
and you want the earlist time
2. You want the earliest time they can meet

Constraints:
are they sorted in anyway? sorted by start time

'''
'''

'''

slotsA = [[6, 8], [5, 10], [10, 50], [60, 120], [140, 210]]
slotsB = [[0,15], [60, 70]]
'''
the reason you need both pointers is because you
need to traverse the first and second array separately
'''
def checkTime(list1, list2, dur):
    overlap = False
    i = 0

    j = 0
    results = []
    '''
         so given the problem above find common ground
         between the 2 things here
     '''


    '''
    Check the pter for i and j 
    '''
    # use the i and j pointer to iterate thru list 1 and list 2
    # do what the guy did in the video
    # as you iterate
    while i <= len(slotsA) -1 and j <= len(slotsB) - 1:

        haveTime = True
        a = slotsA[i]
        b = slotsB[j]
        print('comparring', a, b)
        if (dur > b[1] - b[0]):
            # then inc pter
            j+=1
            haveTime = False

        if (dur > a[1] - a[0]):
            i +=1
            haveTime = False

        if haveTime:
            # then we need to check for overlap

            '''
            [6, 8]
            [60, 70]
            slotsA = [[6, 8], [10, 18], [20, 50], [60, 120], [140, 210]]
slotsB = [[0,15], [60, 70], [22, 29], [] , [] ]
            '''
            # 1st 2 cases no overlap as indicated
            if a[1] < b[0] or b[0] < a[0]:
                print('no overlap')

                ''' 
                when a no overlap is found 
                we need to keep the earlier position time 
                and try to inc the posi
                '''
                '''
                if no overlap then we need to keep 
                the list that has the earlier time
                '''
                # if a[0] < b[0]:
                #     j+=1
                # elif a[0] > b[0]:
                #     i+=1
                j+=1
                i+=1
            # meaning there is an overlap here
            # and have cheded here
            else:

                '''
                the result is found down here 
                '''
                results.append([list1[i], list2[j]])
                print('overlap found')
                break
        else:
            print('passed')




slotsA = [[6, 8], [10, 18], [20, 50], [60, 120], [140, 210]]
slotsB = [[0,15], [22, 31], [60, 70], [] , [] ]
checkTime(slotsA, slotsB, 8)

# if you have 6 and 8 what would it be?
# then you would have