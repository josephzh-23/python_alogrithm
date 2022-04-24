import threading
from datetime import time

# Only sleep for 1 second
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

threads = []

#
#
# 1. Using args to pass sth to the thread
# 2. Look at how the join is done

for _ in range(10):

    t = threading.Thread(target=do_something, args=[1.5])
    t.start()

    #Add the thread here and then
    threads.append(t)

# THis way is very good
for thread in threads:
    thread.join()


