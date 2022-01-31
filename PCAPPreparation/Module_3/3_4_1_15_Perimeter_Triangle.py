import math
from point import Point

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3

    def perimeter(self):
        perimeter = 0.0
        perimeter += self.vertice1.distance_from_point(self.vertice2)
        perimeter += self.vertice1.distance_from_point(self.vertice3)
        perimeter += self.vertice2.distance_from_point(self.vertice3)
        return perimeter

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
