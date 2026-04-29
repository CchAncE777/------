import math

class Vector2D:
    def __init__(self, x, y, deg):
        self._x = x 
        self._y = y
        self._deg = deg

    def __add__(self, other: 'Vector2D'):
        return self._x + other._x, self._y + other._y
    
    def scalar(self):
        return self._x * self._y * math.cos(self._deg)
    
    def __mul__(self, other: 'Vector2D'):
        pass

class Vector3D(Vector2D):
    def __init__(self, z):
        super.__init__()

class VectorND:
    def __init__(self, *args):
        pass

    def __getitem__(self):
        pass

v = VectorND()