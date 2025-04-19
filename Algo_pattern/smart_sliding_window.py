'''

•	If visits = ['home', 'about', 'products', 'contact'] and n = 3, this will produce:
•	['home', 'about', 'products']
•	['about', 'products', 'contact']
'''

visits = ['home', 'about', 'products', 'contact']
n = 3

for i in range(len(visits) - n + 1):
    seq = tuple(visits[i:i+n])

    print(seq)