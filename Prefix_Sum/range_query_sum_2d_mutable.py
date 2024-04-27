'''
         0
 /       |    \       \
1        2     4       8
(0001)  (0010) (0100) (1000)
              /   \
             5    6
           (0101)  (0110)


if you remove the irght most 1 then it becomes 2 here, then it becomes 4
(remove 1 from 0111) it beomces 6 (0110)

And the above makes perfect sense here

ALso important point here:
Can also make the child store the parent node
At node 5, [4, 5] is the relation here


Question 1:
So how to query from value 0 -7

Start from node 7 and then go up to 0
At node 6, we have range sume from [4 -> 6]


'''