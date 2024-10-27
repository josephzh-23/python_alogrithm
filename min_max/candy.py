'''


Candy problem

n children standing in the line

Each child assigned a value rating


Values given to these children here

1) Each child must have at least one candy.
2) Children with a higher rating get more candies than their neighbors.

Clearly another candy problem here we are facing here

'''


def candies(rating):
    left = [1] * len(rating)
    right = [1] * len(rating)

    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            left[i] = left[i - 1] + 1
    # start from 2nd to last child and go back to the first child
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            right[i] = right[i + 1] + 1


    # and then we take the max of each results here

    res = 0
    for item1, item2 in zip(left, right):
        res += max(item1, item2)

    print(left)
    print(right)
    print(res)
ratings = [1, 0, 2]
candies(ratings)
