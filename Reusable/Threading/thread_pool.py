import concurrent.futures
import time

start = time.perf_counter()

# Seconds s a list herex
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'



# Approach 1: we should always use this approach,
# so task comes in when each task finishes

# We can pass in a list here
#   2 methods for using executorpool
with concurrent.futures.ThreadPoolExecutor() as executor:

    #Method 1: using submit
    # We started with 5 seconds
    secs = [5, 4, 3, 2, 1]


    # This is the list compprehension
    results = [executor.submit(do_something, sec) for sec in secs]

    #results are a list here basically
    for f in concurrent.futures.as_completed(results):
        print(f.result())



#Approach 2 better syntax:


'''
Using map, will return based on the order they are started not when
they are finished 

- but using submit, will return based on when they are finished big diffference '''
# with concurrent.futures.ThreadPoolExecutor() as executor:
#
#     #Method 2: using executors.map()   -> return results directly
#     secs = [5, 4, 3, 2, 1]
#     results = executor.map(do_something, secs)
#
#     for result in results:
#         print(result)


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
