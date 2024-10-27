from collections import deque
from typing import List


def removeSubfolders(folder: List[str]) -> List[str]:
    folder.sort()
    dq = deque(folder)
    result = []
    while dq:
        first = dq.popleft()
        print('first is', first)

        '''
        In first iter, result becomes '/a'
        2nd iter:       first : "/a/b"  res: "/a"
            so we use continue to skip over this 
        
        '''
        # the last character is == '/'
        if result and first.startswith(result[-1]):
                # and first[len(result[-1])] == '/':
            continue
        result.append(first)

    print('res is', result)
    return result


folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]

removeSubfolders(folder)