from typing import List


'''
Then here we can see what we can add 

'''
def makesquare(self, matchsticks: List[int]) -> bool:
    if sum(matchsticks) % 4 != 0: return False


    sideLength = sum(matchsticks) // 4
    matchsticks.sort(reverse=True)

    sides = [0, 0, 0, 0]

    def dfs(startIndex):
        if startIndex == len(matchsticks):
            return sideLength == sides[0] == sides[1] == sides[2] == sides[3]

        for i in range(4):


            if sides[i] + matchsticks[startIndex] <= sideLength:
                sides[i] += matchsticks[startIndex]
                if dfs(startIndex + 1): return True

                # the backtrackign happens here
                sides[i] -= matchsticks[startIndex]
        return False
    return dfs(0)