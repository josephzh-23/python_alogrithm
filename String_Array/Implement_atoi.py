
'''

Converts a 32-bt string to a 32-bit signed integer
if s = "42", the answer would be
output : 42


'''


#take care of each cases
def myAtoi(str)-> int:

    str = str.strip()

    if not str:
        return 0
    negative = False
    out = 0

    if str[0] == "-":
        negative = True
    elif str[0] == "+":
        negative= False
    elif not str[0].isnumeric:
        return 0

    # this is the case when it is numeric
    else:
        out = ord(str[0])-ord("0")

    for i in range(1, len(str)):
        if str[i].isnumeric():


            '''
            0
            8
            89
            897
            8978
            '''
            print('the current value is', out)
            out = out*10 + (ord(str[i]) - ord("0"))

            if not negative and out>= 2148483647:
                return 2147483647
            if negative and out >= 2147483648:
                return -2147483648
        else:
            break
    if not negative:
        return out
    else:
        return -out


string = "-89789"

# Function call
print(myAtoi(string))