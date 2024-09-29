
'''

Using the pthon code here you get 

Given 4 points p1 -> p4 and then 


1. Define a helper to calc the distance between all points

2. Calc distances between all points here 

3. Sort the distances here 

4. 

Check if the distances satisfy the conditions of a square:

1) There should be two unique distances (representing side length and diagonal length).

2) The frequency of the side length should be 4, and the frequency of the diagonal length should be 2.

3) The square of the side length should be half of the square of the diagonal length.
'''

def dist(p1, p2):

    # the above is the distance 
    def distance(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p1[2]) ** 2
    

    # You get a combinatino of the distances here and then you have sth next here 

    distances = [distance(p1, p2), distance(p1, p3), distance(p1, p4),
                    distance(p2, p3), distance(p2, p4), distance(p3, p4)]
    distances.sort()

    # check if the unique sides hsould be 2 here
    # 
    # That's it above here  
    distances = set(distances)

    if len(distances) != 2:
        return False
    
    # there could be distances where it's not equal here so be careful of this especially here 
    for i in range(4):
        if distances[i] != distances[0]:

            return False 
        
    # the last 3 should also equal 

    for i in range(4,6):
            if distances[i]!=distances[5]:
                return False
        
    if distances[0] * 2 != distances[5]:
        return False
    
    return True 