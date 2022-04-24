#
#
# def tryCatch(func):
#    def silenceit(*args, **kwargs): # takes all kinds of arguments
#       try:
#          return func(*args, **kwargs) # returns func's result
#       except Exception as e:
#          print('Error:', e)
#          return e # not the best way, maybe we'd better return None
#                   # or a wrapper.py object containing e.
#   # return silenceit # on the correct level
# aer =False
# tryCatch(print(10*(1/0)))

def f1(func):

    # Can take any input then
    def wrapper(*args, **kwargs):
        print("started")
        func(*args, **kwargs)
        print("end")

    # Return the function that runs
    return wrapper

def f():
    print("hello")

# How to run the above func without decorator


f1(f)()
# x = f1(f)