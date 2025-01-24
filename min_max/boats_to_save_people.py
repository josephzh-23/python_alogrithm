'''
Bostas to save people
https://leetcode.com/problems/boats-to-save-people/description/

Each boat max weight of limit
people with weight [i]
weight of ith person

Inifite # of boats to carry any people,
Each boat can carry the limit given in the problem

people 1: 3
(1, 2)

people = [3, 2, 2, 1]
limit = 3

so sort this and becomes

[1, 2, 2, 3]
limit = 3

So we keep pariing the boats to see if anything falls within the limit
i = 0   j = 3
sum = people[i] + people[j] = 4 > limit
so j -= 1
total = 1

i = 0   j = 2
sum = people[i] + people[j] = 3 = limit
so j -= 1
i +=1
total = 2

i = 1 j = 1
now only 1 left
so one more boat

So the total is 3
3 boats (1, 2), (2) and (3)

These make a lot of sense here now

Using a 2 people approach here works

Can check out the solution on algomonster
'''

def getPeopleSave(people, limit):
    people.sort()