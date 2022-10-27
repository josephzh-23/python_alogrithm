from typing import List


def reorderLogFiles(logs: List[str]) -> List[str]:

    # will contain some strings here
    digits = []

    # will contains sth like pair<String, string>
    letters = dict()

    mp = dict()
    for i in range(len(logs)):
        mp[logs[i]] +=1

    # as you filter thru the logs here
    for log in logs:
        spaceIdx = -1

        for i in range(len(log)):
            if log[i] == ' ':
                spaceIdx = i
                continue

                # that means there is a space in the log here
            if spaceIdx != -1:
                if log[i] - '0' >=0 and 
if __name__ == '__main__':
    # logs = [input() for _ in range(int(input()))]
    # res = reorderLogFiles(logs)
    # for line in res:
    #     print(line)
    logs = ["ykc 82 01",
            "eo first qpx"]
    reorderLogFiles(logs)
    # [eo first qpx]
    # [09z cat hamster]
    # [06f 12 25 6]
    # [az0 first qpx]
    # [236 cat dog rabbit snake]
