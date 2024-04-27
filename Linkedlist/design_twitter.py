import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.createdTime= 0 # created time
        self.tweetMap = defaultdict(list) # userId -> list of [createdTime, tweetids]
        self.followMap = defaultdict(set) # userId -> set of followeeId

        '''
        Part 1: tweetMap [here ] 
        
        userID: [count, tweetIds] 
        
        Part 2: 
        With the follow map it will then be as sth like the following 
        1 : [1, 2] this is quite important 
        followerId : [followeeId] here 
        
        '''

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    '''
    Return the 10 most recently tweet ids in the user's nees feed, 
    
    '''
    def getNewsFeed(s, userId: int) -> List[int]:

        res = []
        minHeap = []
        # use minheap to store the tweets here
        '''
        If we have k user Id , will take O(log k)

        '''
        # subscribe first here
        s.followMap[userId].add(userId)

        # add each of the [count, tweetId, followeeId, index -1] to this
        for followeeId in s.followMap[userId]:


            if followeeId in s.tweetMap:
                index = len(s.tweetMap[followeeId]) - 1
                count, tweetId = s.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])

        heapq.heapify(minHeap)
        '''
        We are trying to build a minHeap here based on teh time in which it was inserted
        
        '''
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = s.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

        #return a list with id 1
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

