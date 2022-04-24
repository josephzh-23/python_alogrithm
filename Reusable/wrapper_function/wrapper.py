def func(f):

    def wrapper(*args, **kwargs):
        print("started")
        rv = f(*args, **kwargs)
        print("ended ")
        return rv

    return wrapper

@func
def func2(x, y):
    print(x)
    return y

x = func2(5, 6)
print(x)










