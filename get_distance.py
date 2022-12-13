import math

def dist_2d(p1,p2):

    distance = (math.sqrt( ((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2) ))
    return(distance)

print(dist_2d([4,0], [0,3]))
print(dist_2d([5,2], [1,5]))

