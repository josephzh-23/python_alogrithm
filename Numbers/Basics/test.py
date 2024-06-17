'''


'''

def func(num):
    digit_sum = 0

    if num < 10:
        return num

    while num:
        digit_sum += num % 10
        num = num // 10
        print('number is', digit_sum)
func(32)