


'''
generate partition for each label down here and above there

'''

def partitionLabel(s):


# will get the position of last element seen up till now
    last = [0] * 26

    # so you find the last position of each character here
    for i, c in enumerate(s):
        print("index is " , i)
        last[ord(c) - ord('a')] = i


    print("last value is " , last)

    '''
    The anchor and j will be the starting and last position of 
    the current partition, 
    
    If we are at a label that occurs last at some inex after j, 
    extend the j = last[c] here 
    
    '''
    j, anchor = 0, 0
    # and then

    ans = []

    for i in range(0, len(s)):

        ''' 
        will be 8 or sth, 
        
        '''
        j = max(j, last[ord(s[i]) - ord('a')])

        if (i == j):
            ans.append(i - anchor + 1)
            anchor = i + 1

    print("answer is ", ans)
    return ans




partitionLabel("ababcbacadefegdehijkhlij")







