from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        self._radius = radius

    def perimetr(self):
        return self._radius * 2 * math.pi

    def area(self):
        return (self._radius ** 2) * math.pi

class Square(Figure):
    def __init__(self, side):
        self._side = side

    def perimert(self):
        return self._side * 4
    
    def area(self):
        return self._side ** 2

class Trapezoid(Figure):
    def __init__(self, footing_1, side_1, footing_2, side_2):
        self._footing_1 = footing_1
        self._side_1 = side_1
        self._footing_2 = footing_2
        self._side_2 = side_2

    def perimetr(self):
        return self._side_1 + self._footing_1 + self._side_2 + self._footing_2
    
    def area(self):
        part_1 = (self._footing_1 + self._footing_2) / 2
        if self._side_1 > self._side_2:
            part_2 = self._side_1 ** 2
        else: 
            part_2 = self._side_2 ** 2
            if self._footing_2 > self._footing_1:
                self_part_3 = (((self._footing_2 - self._footing_1) ** 2) + self._side_2 ** 2 - self._side_1 ** 2) / (self._footing_2 ** 2 - self._footing_1 ** 2)
            else:
                pass
        return 
        
    
class rectangle(Figure):
    def __init__(self, side_1, side_2):
        self._side_1 = side_1
        self._side_2 = side_2

    def perimert(self):
        return self._side_2 * 2 + self._side_1 * 2
    
    def area(self):
        return self._side_1 * self._side_2


class Triangle(Figure):
    def __init__(self, side_1, side_2, side_3):
        self._side_1 = side_1
        self._side_2 = side_2
        self._side_3 = side_3

    def perimetr(self):
        return self._side_1 + self._side_2 + self._side_3
    
    def area(self):
        p = (self._side_1 + self._side_2 + self._side_3) / 2
        return math.sqrt((p) * (p - self._side_1) * (p - self._side_2) * (p - self._side_3))
    
print(Circle(3).perimetr())