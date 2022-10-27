

# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold
#
logs = ["88 99 200", "88 99 300", "99 32 100" ]
def processLogs(logs, threshold):

    res= []
    #check the threshold
    users= {}
    # logs will be a list so break it down first
    for item in logs:
        item = item.split(" ")

        sender = item[0]
        receiver = item[1]

        # case 1
        if sender == receiver:
            if sender not in users:
                users[sender] =1
            else:
                users[sender]+=1

        # case 2
        else:
            if sender not in users:
                users[sender] = 1
            else:
                users[sender] += 1

            if receiver not in users:
                users[receiver] = 1
            else:
                users[receiver] += 1

    # print(users.items())

    for user, count in users.items():
        if count > threshold:
            res.append(user)

    return res

res = processLogs(logs, 2)
print(res)