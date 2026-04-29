def func1(*args):
    s = 0
    for a in args:
        s += a
    return s

print(func1(1, 2, 3, 4))

def func2(**kwargs):
    pass

class Vector2D:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __lt__(self, other):
        return self._x < other._x
    
    def __repr__(self):
        return f'({self._x}, {self._y})'

    def lenght(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5

l: list[Vector2D] = [
    Vector2D(1, 2),
    Vector2D(2, 6),
    Vector2D(1, 0)
]

print(l[0] < l[1])

print(sorted(l, key = lambda v: v.lenght))


