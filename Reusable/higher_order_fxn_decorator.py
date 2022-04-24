def tryCatchWithReturn(func):
    # Can take any input then

    #With args and kwargs, we can have any number of arguments
    def wrapper(*args, **kwargs):
        try:
            print("try catch block")
            val = func(*args, **kwargs)
            return val
        except Exception as e:
            print("exception: " + str(e))

    # Return the function that runs
    return wrapper


def f():
    print("hello")


# tryCatch(f)()
