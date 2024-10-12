'''


How to solve this problem here

citations = [3,0,6,1,5]

5 paper here and each got
5 in total here and there
# of citations a researcher received

max vaue

At least h papers

has been cited at least h times
'''

def hasAtLeastHPapersWithCitations(h, citations):
    count = 0
    for count in citations:
        if count >= h:
            count+=1
    return count >=h


low = 0