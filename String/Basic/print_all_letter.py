# Python program to print
# Alphabets from A to Z

# Declare the variable
i = 'a'

# Display the alphabets
"The Alphabets from A to Z are:"

# Traverse each character
# with the help of a while loop
while ord(i) <= ord('z'):
    i = chr(ord(i) + 1)
    print(i)