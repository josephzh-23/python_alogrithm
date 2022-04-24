import threading
import time



start = time.perf_counter()
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

#Basic threading here
#Using baisc threading, target -> fxn name
t1 = threading.Thread(target = do_something(1))
t2 = threading.Thread(target = do_something(1))

t1.start()
t2.start()

#Will then just block the thread
t1.join()
t2.join()
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} seconds(s)')



#To run the function here

threads = []

# for _ in range(10):
#
#     #target is the functino that we want to run
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()
#
# finish = time.perf_counter()
#
# print(f'Finished in {round(finish-start, 2)} second(s)')