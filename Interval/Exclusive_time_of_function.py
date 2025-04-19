


def exclusiveTime(n, logs):
    # keep track of the function ids here
    callstack = []

    exclusiveTimes = [0] * n
    currentTime = -1

    # process each log here in the code
    for log in logs:
        parts = log.split(':')

        fxnId, startOrEnd, timestamp = parts
        if startOrEnd == 'start':

            '''
            if there is an ongoing event, and then we add the timestamp to the previous fucntionId
            '''
            if callstack:
                exclusiveTimes[callstack[-1]] += timestamp

                # push the current unto the stack
                callstack.append(fxnId)

                # udpate the current time
                currentTime = timestamp

        # an end event
        else:
            fxnId = callstack.pop()
            exclusiveTimes[fxnId] = timestamp - currentTime +1

            # Update the current time to the end time + 1 since the next time unit
            # will indicate the start of the next event.
            currentTime = timestamp + 1
    return exclusiveTimes