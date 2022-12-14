# Component 6 of main: distance to measure points between n-dimension
import math

# 2-dimension
def dist_2d(p1,p2):

    distance = ((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2)

    return math.sqrt(distance)

print(dist_2d([4,0], [0,3]))
print(dist_2d([5,2], [1,5]))

# n-dimension
def dist(p1,p2):
    distance = 0
    for index in range(len(p1)):
        distance += (p1[index] - p2[index])**2
    return math.sqrt(distance)
print(dist([4, 0, 3, 6, 1], [0, 3, 0, 5, 0]))