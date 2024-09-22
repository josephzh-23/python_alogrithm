'''

Tracl the video with highest cont for each creator


Use dict to store cumulative views and keep track of the most popular video for each creator

used a dictionary (mapped_data) where the key is the creator's name, and the value is a list containing the total views,
the ID of the most viewed video, and the view count of that video.
'''
from collections import defaultdict

from Heap.max_heap import MaxHeap


def solution(creators, ids, views):


    # keep track of the max view here
    maxView = 0
    nameTotalViews = dict()
    #associated with the video with most views

    nameToMaxViewCount = defaultdict(list)
    for c, id, numberOfView in zip(creators, ids, views):

        # if view needs to be udpated then we have to update it

        maxView = max(maxView, numberOfView)
        # {alice: [5, 'one']
        print('this is', nameToMaxViewCount)
        if nameToMaxViewCount[c]:
            print('yes')

            print(nameToMaxViewCount[c][0])
        #
            ans = nameToMaxViewCount[c]
            ans = ans[0]
            if ans < numberOfView:

                print('this is ', numberOfView, id)
                nameToMaxViewCount[c] = [numberOfView, id]
        # else:
        #     nameToMaxViewCount[c] = [numberOfView, id]
        # print(nameToMaxViewCount)
        else:
            nameToMaxViewCount[c] = (numberOfView, id)
        # print('the name is',nameToMaxViewCount[c])

        # for the total view
        nameTotalViews[c] = numberOfView + nameTotalViews.get(c, 0)

    # now we just get all the names with highest keys here
    # max
    nameWithMostViewedVideo = []
    for name, number in nameTotalViews.items():
        if number == maxView:
            nameWithMostViewedVideo.append([name, nameToMaxViewCount[name][1]])
    # print(nameTotalViews)
    # print(nameToMaxViewCount)

    return nameWithMostViewedVideo

    #example 1 here passed!
creators = ["alice","bob","alice","chris"]
ids = ["one","two","three","four"]
views = [5,10,5,4]

creators = ["alice", "alice", "alice"]
ids = ["a", "b", "c"]
views = [1, 2, 2]

solution(creators, ids, views)