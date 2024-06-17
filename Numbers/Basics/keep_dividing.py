# how to keep dividing here

# and then we have the code

'''

fun intToRoman(num: Int): String {
    var num = num
    while(num > 0){

        num /= 10
        println(num)
        // so you will then get 15, 1 and so forth here
    }
    return " "
}
'''

def intToRoman(num):

    # this makes sure the number is not 0 here 
    while num:
        num = num // 10
        print(num)

intToRoman(123)

