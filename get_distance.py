import math

def dist_2d(p1,p2):

    distance = (math.sqrt( ((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2) ))
    return(distance)

print(dist_2d([4,0], [0,3]))
print(dist_2d([5,2], [1,5]))

def dist(p1,p2):
    result = 0
    for index in range(len(p1)):
        print(index)
        result += (p1[index] - p2[index])**2
    return math.sqrt(result)
print(dist([4, 0, 3, 6, 1], [0, 3, 0, 5, 0]))
