


def tryCatch(func):

    # Can take any input then
    def wrapper(*args, **kwargs):
        try:
            print("try catch block")
            func(*args, **kwargs)
        except Exception as e:
            print("exception: " + str(e))

    # Return the function that runs
    return wrapper

def f():
    print("hello")
tryCatch(f)()
