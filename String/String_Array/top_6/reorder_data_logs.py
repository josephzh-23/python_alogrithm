'''
logs = ["dig1 8 1 5 1",
"let1 art can",
"dig2 3 6",
            "let2 own kit dig","let3 art zero"]
Output: ["let1 art can",
"let3 art zero",
"let2 own kit dig",
"dig1 8 1 5 1",
"dig2 3 6"]

# basically there are 2 types the first

# the time complexity here is O (nlog(n)) because of sorting
'''
from typing import List


def reorderLogFiles(logs: List[str]) -> List[str]:
    '''
    Once we are done with the type, our pty will be based on the letters

    Once done combine the letter log array + digit log array
    digit logs retain ordering
    '''
    # res1
    res1, res2 = [], []

    for log in logs:
        if log.split()[1].isdigit():
            res2.append(log)
        else:
            res1.append(log.split())

    # here sort the result by the identifier first
    print(res1)

    # sort each string in the array by the second element
    res1.sort(key = lambda x:x[1])
    print(res1)
    for i in range(len(res1)):
        res1[i] = (" ".join(res1[i]))

    print(res1)
    # print(res2)
    res1.append(res2)

    # need to figure out how to sort byt



logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
reorderLogFiles(logs)