'''



'''
from Queue_heap.max_heap import MinHeap



def answer(s):
    letterHeap = MinHeap()
    res = ""


    res += s[0]
    numHeap = MinHeap()
    if s[0].isalpha():
        letterHeap.push(s[0])
    if s[0].isnumeric():
        numHeap.push(s[0])
    for i in range(0, len(s) - 1):
        if s[i].isalpha() and s[i + 1].isalpha():
            print('this is', s[i + 1])
            letterHeap.push(s[i + 1])
            # res += s[i]

            if numHeap.__len__() > 0:
                res += numHeap.pop()
        elif s[i].isnumeric() and s[i + 1].isnumeric():
            print('that is', s[i + 1])

            numHeap.push(s[i + 1])
            # res += s[i]

            if letterHeap.__len__() > 0:
                res+=letterHeap.pop()

            " the case 'b1'  "

        # elif s[i +1].isnumeric():
        #     print('this is 3rd', s[i + 1])
        #     res+=s[i + 1]
        # elif s[i + 1].isalpha():
        #     print('this is 4th', s[i + 1])
        else:
            print('come here', s[i + 1])
            res+=s[i + 1]
    print(res)

input = "aabb12cc345"
answer(input)