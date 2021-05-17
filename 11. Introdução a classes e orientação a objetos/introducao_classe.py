# Nome de classe com letra maiúscula
from math import sqrt

class Point:

  def __init__(self, vx, vy):
    self.x = vx
    self.y = vy

  def distance_to(self, other_point):
    return sqrt((self.x - other_point.x)**2 + \
    (self.y - other_point.y)**2)

p1 = Point(2, 3)
p2 = Point(4, 5)

dist = p1.distance_to(p2)

print(dist)