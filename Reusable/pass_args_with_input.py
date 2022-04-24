

# used to get the object posting for now
def tryCatchWithReturn2(func):
    try:
        print("try catch block")
        val = func

        #Keep it like above with func instead of func() and better that way
        return val
    except Exception as e:
        print("exception: " + str(e))


#
# def perform(fun, *args):
#     fun(*args)
#
# def action1(args):
#     # something
#
# def action2(args):
#     # something
#
# perform(action1)
# perform(action2, p)
# perform(action3, p, r)


