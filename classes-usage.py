class Rectangle:
    def __init__(self, h, w):
        self.h = h
        self.w = w

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, h):
        if h < 0:
            raise ValueError('Height cannot be negative')
        else:
            self._h = h

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, w):
        if w < 0:
            raise ValueError('Width cannot be negative')
        else:
            self._w = w

    def area(self):
        return self.h * self.w

    def __str__(self):
        return 'Rectangle with Width: {}, Height: {}'.format(self.w, self.h)

    def __repr__(self):
        return 'I\'m  Rectangle with Width: {}, Height: {}'.format(self.w, self.h)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.h == other.h and self.w == other.w
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


"""
If we want to restrict negative values being given to side we can either go with a setter method
or a decorator

If you want a property to be private you can just declare it with an "_" inside the __init__() with
no Setter & Getter methods (if you dont want to modify the value, if you just want the property to be
private and want to change the values, use getteer and setter)
"""


class Square:
    def __init__(self, side):
        self.side = side

    """Getter Method"""
    @property
    def side(self):
        return self._side

    """Setter Method"""
    @side.setter
    def side(self, side):
        if side < 0:
            raise ValueError('OOPS! Error: side needs to be a positive value')
        else:
            self._side = side

    def __str__(self):
        return 'Square with Side: {}'.format(self.side)


"""Getter and Setter Methods - Not an ideal way to use as below"""
# def get_side(self):
#     return self._side

# def set_side(self, side):
#     if side < 0:
#         raise ValueError('Side must be positive')
#     else:
#         self._side = side


r1 = Rectangle(4, 5)
r2 = Rectangle(4, 5)
r1.h = -3
print(r1)


s1 = Square(-1222)
s1.side = -122
print(s1)

print(r1 == s1)
