class Shape:
    def area(self):
        return 0
class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w
l, w = map(int, input().split())
o = Rectangle(l, w)
print(o.area())