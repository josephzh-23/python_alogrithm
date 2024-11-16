'''

How to solve this problem here

Opeartions[i]

An integer x here

+

C invalidate prev score

D record of previous double
'''


def solution(nums):
    st = []
    for x in nums:
        if x.isdigit():
            st.append(x)
        if x == "C":
           st.pop()

        if x == "D":
            res = int(st[-1]) * 2
            st.append(res)

        # if it's adding here then we have
        if x == "+":
            res = int(st[-1])  + int(st[-2])
            st.append(res)

    print('st is ', st)

solution(["5","2","C","D","+"])



