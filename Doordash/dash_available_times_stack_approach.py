'''


res = 0
have a stack..

if its pick up, push time to stack
if its drop off, pop from stack. if stack is empty, subtract the dropoff from the currently popped off time(pick up) and add it to res

return res
'''


class Activity:
    def __init__(self, time, a):
        self.time = time
        self.a = a


def get_active_time(activity):
    stack = []
    res = 0

    for i in range(len(activity)):
        if activity[i].a == 'p':
            stack.append(activity[i])

            '''
            Basically if drop off we keep drop off until no more drop off and then - the appointment time last here 
            
            '''
        else:
            popped_act = stack.pop()
            if not stack:
                res += activity[i].time - popped_act.time

    return res


def get_activities(activity):
    activities = []

    for s in activity:
        strs = s.split("|")

        act = 'p' if strs[1].strip() == "pickup" else 'd'
        activities.append(Activity(get_time(strs[0].strip()), act))

    return activities


def get_time(time):
    index_of_colon = time.index(":")
    hour = int(time[:index_of_colon]) % 12 * 60
    min = int(time[index_of_colon + 1:index_of_colon + 3])

    if "pm" in time:
        hour += (60 * 12)

    return hour + min


if __name__ == "__main__":
    activity = [
        "8:30am|pickup",
        "9:10am|dropoff",
        "10:20am|pickup",
        "12:15pm|pickup",
        "12:45pm|dropoff",
        "2:25pm|dropoff",
    ]

    acts = get_activities(activity)
    print(get_active_time(acts))

