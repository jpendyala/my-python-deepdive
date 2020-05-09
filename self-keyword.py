class Rectangle:
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def area(self):
        return self.h * self.w

r1 = Rectangle(4, 5)
print(r1.area())
