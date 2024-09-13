from collections import Counter

# this is the brute force approach
def numFriendRequests(ages):
    counter = Counter(ages)
    ans = 0

    print('counter is', counter)
    # ({16: 1, 17: 1, 18: 1})       this is very effective here
    # and then we have the code
    for ageA, countA in enumerate(counter):       # nested loop, pretty straightforward
        for ageB, countB in enumerate(counter):
            if isFriendRequest(ageA, ageB):
                ans += countA * countB
                # in the case of 16, 16 then we can use this formula here
                # that's it 
                if ageA == ageB: ans -= countA
    return ans


def isFriendRequest(a, b):
    if b <= 0.5 * a + 7: return False
    if b > a: return False
    return True
numFriendRequests([16,16])