# How to use the global variable in fxn in python?
'''
 need to use global df inside fxn that modfiied the global variable
otherwise you are creating a local scoped variable of same name
inside the function, and your changes won't be reflected

Ex
'''
p = "bka"
def func():
    print("print from func:", p)      # works, readonly access, prints global one

def func2():

    # This allows you to modify the variable global
    global p
    p = "blubb"  # modifies the global p
