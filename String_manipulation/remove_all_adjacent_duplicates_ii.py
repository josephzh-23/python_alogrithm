'''


Here is how the code works:

Initializing the Stack: We begin by initializing an empty list "stk" which will serve as our stack. The stack will store sublists where each sublist contains a character and a count of how many times it has occurred consecutively.


The top comparison here:
Iterating Over the String: We iterate over each character "c" in the string "s":

Top of the Stack Comparison: We look at the top element of the stack (if it isn't empty) to see if c is the same as the character at the top of the stack (stk[-1][0] represents the character at the top of the stack).


Incrementing Count:
 If the top element is the same as c, we increment the count (stk[-1][1]) and check if this count has reached k. If the count is k, this signifies a k duplicate removal, and therefore we pop the top of the stack.

    Kind of like accumulating here

Pushing New Characters:
If the stack is empty or c is different from the top character of the stack, we push a new sublist onto the stack with c and the count 1.


Reconstructing the String:

After the iteration, the stack contains characters that did not qualify for k duplicate removal, with their counts being less than k. Now, to reconstruct the final string, we multiply (*) each character c by its count v and join ("".join()) the multiplied strings to form the answer.


The mathematical formula for the reconstruction process is given by:
ans = "".join([c * v for c, v in stk])



Implementation here:


1) Part 1
if stk and stk[-1][0] == c:
 This checks if the stack is not empty and whether the top element on the stack is the same as the current character.

stk[-1][1] = (stk[-1][1] + 1) % k: Here, we increment the count and use the modulus operator to reset it to 0 if it reaches k (since k % k is 0).

part 2 :
if stk[-1][1] == 0: stk.pop(): If after incrementing, the count becomes 0, meaning we have k duplicates, we remove (pop) the top element from the stack.
else: stk.append([c, 1]): In case the character c is different or the stack is empty, we append c along with the initial count 1 as a new group in the stack.


ans = [c * v for c, v in stk]: We build the answer list by multiplying the character c by its count v.
return "".join(ans): Join all strings in the ans list to get the final answer.
The code takes advantage of Python's built-in list operations to simulate stack behavior efficiently, making the solution succinct and highly readable.


Look at the data structure and then you can do the following here
Input	Stack	Operation
'a'	[('a', 1)]	Push 'a'
'a'	[('a', 2)]	Increment count of 'a'
'b'	[('a', 2), ('b', 1)]	Push 'b'
'b'	[('a', 2), ('b', 2)]	Increment count of 'b'
'b'	[('a', 2)]	Increment count of 'b' and remove 'b' as count==k
'a'	[]	Increment count of 'a' and remove 'a' as count==k
'c'	[('c', 1)]	Push 'c'
'c'	[('c', 2)]	Increment count of 'c'

'''

def solution(string, k):
    st = []
    res = ""
    for c in string:
        if st:
            if c != st[-1][0]:
                st.append((c, 1))

                '''
                The same case here 
                '''
            else:
                existingCount = st[-1][1]
                existingCount+=1

                if existingCount !=k:
                    st.append((c, existingCount))
                else:
                    st.pop()
        else:
            st.append((c, 1))

    for c, v in reversed(st):
        res+=c
    print(res)

solution()



