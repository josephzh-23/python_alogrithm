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
Create directed edegs  

{'Earth': [['North America', 'South America']],
     'North America': [['South America'], ['United States', 'Canada']], 

     'South America': [[], ['Brazil']], 
     'United States': [['Canada'], ['New York', 'Boston']], 
     'Canada': [[], ['Ontario', 'Quebec']], 

'New York': [['Boston']], 
'Boston': [[]], 

'Ontario': [['Quebec']],
 'Quebec': [[]], 'Brazil': [[]]}
'''


def solution(regions, region1, region2):
    edges = collections.defaultdict(list)
    for region in regions:
        for reg in region:
            k = len(reg)
            print(reg)

            for j in range(0, k):
                edge = reg[j]

                edges[edge].append(reg[j + 1:k])

    print(edges)


regions = [["Earth", "North America", "South America"],
           ["North America", "United States", "Canada"],
           ["United States", "New York", "Boston"],
           ["Canada", "Ontario", "Quebec"],
           ["South America", "Brazil"]],
region1 = "Quebec",
region2 = "New York"

solution(regions, region1, region2)
















