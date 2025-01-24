'''

The challenge is to compare two version numbers, version1 and version2. A version number is a sequence of numbers
separated by dots, with each number called a revision. The task is to compare the version numbers revision by
revision, starting from the left (the first revision is revision 0, the next is revision 1, etc.).

Input: version1 = "1.2", version2 = "1.10"


'''

# this is a brute force solution here
def sol(v1, v2):

    v1 = v1.split('.')
    v2 = v2.split('.')


    p1 = p2 = 0
    while p1 < len(v1) and p2 < len(v2):
        if v1[p1] != v2[p2]:
            s1 = v1[p1]
            s2 = v2[p2]

            len1= len(s1)
            len2 = len(s2)
            index = 0
            number1 ,number2= '', ''

            # get number1 here and then compare here
            while index < len1 and s1[index].isdigit():
                number1 += str(s1[index])
                index += 1
            print('number 1 is', number1)
            index = 0
            while index < len2 and s2[index].isdigit():
                number2 += str(s2[index])
                index += 1
            print('number 2 is',number2)

            print('which one is bigger', int(number1)==int(number2))
        p1+=1
        p2+=1

version1 = "1.1";version2 = "1.30"
sol(version1, version2)