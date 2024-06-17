months = {"Jan": 1,
          "Feb": 2,
          "Mar": 3,
          "Apr": 4,
          "May": 5,
          "Jun": 6,
          "Jul": 7, 'Aug': 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

# years in the range
years = [1900, 2100]
'''
Convert the date to the format yyyy-mm-dd where 

'''


# print('Oct' in months.values())

def answer(string):
    final = ''
    temp = ''
    for c in string:
        if c != ' ':
            temp += c
            print(temp)
            if temp.isdigit():
                final += temp
                temp = ''
            elif temp in months:
                print('month is ', months.get(temp))
                final += str(months[temp])
                temp = ''
            elif 'th' in temp:
                temp = temp.strip('th')
                final += temp
                temp = ''
        elif c == ' ':
            final += '-'


    print(final)


answer("20th Oct 2052")
