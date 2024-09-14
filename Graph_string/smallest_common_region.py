'''

To work on this problme here

Regions: include other reginos
X : y   X a parent of itself

Region 1: Quebec
Region 2: New york here
Smallest regions that contain both of them?

'''
import collections

'''

'''
def solution(regions, region1, region2):

    # Build a family tree from offspring to their parents here

    parents = collections.defaultdict()
    ancestorHistory = set()

    '''
    regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],

    Earth would be the parent of North America and also South America 
    
    '''
    for region in regions:
        for i in range(1, len(region)):

            # and the above is what makes sense here
            parents[region[i]] = region[0]

    print(parents)
    # we keep adding the ancestory history tree here
    while region1 in parents:
        region1 = parents[region1]
        ancestorHistory.add(region1)
    while region2 not in ancestorHistory:
        region2 = parents[region2]
    return region2


regions = [["Earth", "North America", "South America"],
           ["North America", "United States", "Canada"],
           ["United States", "New York", "Boston"],
           ["Canada", "Ontario", "Quebec"],
           ["South America", "Brazil"]]
region1 = "Quebec"
region2 = "New York"
# Output: "North America"

print(solution(regions, region1, region2))









